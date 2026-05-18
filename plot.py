"""
plot.py
Visualización.
"""

import matplotlib.pyplot as plt



def plot_results(history):
    """
    Fitness vs iteraciones.
    """

    plt.plot(history)

    plt.xlabel("Iteraciones")

    plt.ylabel("Fitness")

    plt.title("Fitness vs Iteraciones")

    plt.grid()

    plt.show()