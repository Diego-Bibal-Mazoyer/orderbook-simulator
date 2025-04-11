# Order Book Simulator

Ce projet est un simulateur de carnet d’ordres en temps réel basé sur un processus de Hawkes. Il permet de modéliser dynamiquement l’arrivée des ordres d’achat et de vente, de les gérer dans un carnet d’ordres et de visualiser les interactions de manière interactive grâce à une interface Streamlit.

## Objectifs

- Simuler l’arrivée dynamique des ordres d’achat et de vente à l’aide d’un modèle stochastique.
- Gérer les ordres dans un carnet d’ordres avec une logique réaliste d’exécution et d’annulation.
- Afficher le carnet d’ordres en temps réel et visualiser les résultats des transactions dans une interface graphique.
- Analyser les résultats via des statistiques sur les temps d’arrivée des ordres, la profondeur du carnet, et la fréquence des trades.

## Structure du projet

```plaintext
project_orderbook/
├── models/
│   └── hawkes.py               # Modélisation du processus de Hawkes
├── simulator/
│   ├── orderbook.py            # Gestion du carnet d’ordres
│   └── events.py               # Simulation des événements d’arrivées d’ordres
├── analysis/
│   └── statistics.py           # Analyse statistique des résultats
├── interface/
│   └── app.py                  # Application Streamlit pour l'interface interactive
├── requirements.txt            # Liste des dépendances
└── README.md                   # Documentation du projet

