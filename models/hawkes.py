# models/hawkes.py

from tick.hawkes import SimuHawkesExpKernels
import numpy as np

def simulate_hawkes(mu=0.2, alpha=0.5, beta=1.0, duration=1000):
    """
    Simule un processus de Hawkes à noyaux exponentiels.

    Paramètres :
    - mu : intensité de base (baseline)
    - alpha : intensité de rétroaction (auto-excitation)
    - beta : taux de décroissance
    - duration : durée de la simulation

    Retour :
    - Liste des timestamps simulés
    """
    hawkes = SimuHawkesExpKernels(baseline=[mu],
                                  adjacency=[[alpha]],
                                  decays=[[beta]],
                                  end_time=duration,
                                  seed=123)
    hawkes.simulate()
    return hawkes.timestamps[0]


