from models.hawkes import simulate_hawkes
from simulator.orderbook import OrderBook
import numpy as np

# Génère des timestamps Hawkes
timestamps = simulate_hawkes(duration=100)

# Génère des prix / volumes / sides fictifs
np.random.seed(42)
prices = np.random.normal(100, 1, len(timestamps))
volumes = np.random.randint(1, 10, len(timestamps))
sides = np.random.choice(['bid', 'ask'], len(timestamps))

# Init carnet et injecte les ordres
orderbook = OrderBook()
for t, price, volume, side in zip(timestamps, prices, volumes, sides):
    orderbook.add_order(price, volume, side)

# Affiche les trades
trades = orderbook.match_orders()
print("Exécution des trades :")
for trade in trades:
    print(trade)

# Affiche les carnets restants
print("\nBids restants :", orderbook.bids)
print("Asks restants :", orderbook.asks)

