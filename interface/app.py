import sys
import os

# Ajouter la racine du projet au PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
from simulator.orderbook import OrderBook
from models.hawkes import simulate_hawkes
import numpy as np
import pandas as pd

st.title("Simulateur de Carnet d'Ordres avec Hawkes")

duration = st.slider('Durée de simulation (secondes)', 100, 10000, 1000)

timestamps = simulate_hawkes(duration=duration)

orderbook = OrderBook()

# Simuler rapidement les prix et les volumes pour illustrer :
np.random.seed(42)
prices = np.random.normal(100, 1, len(timestamps))
volumes = np.random.randint(1, 10, len(timestamps))
sides = np.random.choice(['bid', 'ask'], len(timestamps))

for t, price, volume, side in zip(timestamps, prices, volumes, sides):
    orderbook.add_order(price, volume, side)

trades = orderbook.match_orders()

spreads = []
depths = []
time_axis = []

for i, (t, price, volume, side) in enumerate(zip(timestamps, prices, volumes, sides)):
    orderbook.add_order(price, volume, side)
    orderbook.match_orders()
    
    # Prend meilleur ask et meilleur bid si dispo
    if orderbook.bids and orderbook.asks:
        best_bid = orderbook.bids[0]['price']
        best_ask = orderbook.asks[0]['price']
        spread = best_ask - best_bid
        depth = len(orderbook.bids) + len(orderbook.asks)
        
        spreads.append(spread)
        depths.append(depth)
        time_axis.append(t)


st.write("Trades exécutés :", pd.DataFrame(trades))

st.subheader("Carnet d'ordres final")
col1, col2 = st.columns(2)
col1.write("**Bids**")
col1.write(pd.DataFrame(orderbook.bids))
col2.write("**Asks**")
col2.write(pd.DataFrame(orderbook.asks))

import plotly.express as px
import pandas as pd

# Créer un DataFrame pour les trades
df_trades = pd.DataFrame(trades)

# 📈 Histogramme des prix des trades
if not df_trades.empty:
    st.subheader("Distribution des prix des trades")
    fig_price = px.histogram(df_trades, x="price", nbins=30, title="Histogramme des prix")
    st.plotly_chart(fig_price, use_container_width=True)

    # 📊 Histogramme des volumes
    st.subheader("Distribution des volumes des trades")
    fig_volume = px.histogram(df_trades, x="volume", nbins=10, title="Histogramme des volumes")
    st.plotly_chart(fig_volume, use_container_width=True)



import plotly.graph_objects as go

st.subheader("📊 Analyse dynamique")

# ➤ Spread
fig_spread = go.Figure()
fig_spread.add_trace(go.Scatter(x=time_axis, y=spreads, mode='lines', name='Spread'))
fig_spread.update_layout(title='Évolution du spread', xaxis_title='Temps', yaxis_title='Spread')
st.plotly_chart(fig_spread, use_container_width=True)

# ➤ Profondeur
fig_depth = go.Figure()
fig_depth.add_trace(go.Scatter(x=time_axis, y=depths, mode='lines', name='Profondeur'))
fig_depth.update_layout(title='Profondeur du carnet au fil du temps', xaxis_title='Temps', yaxis_title='Nombre d’ordres')
st.plotly_chart(fig_depth, use_container_width=True)

