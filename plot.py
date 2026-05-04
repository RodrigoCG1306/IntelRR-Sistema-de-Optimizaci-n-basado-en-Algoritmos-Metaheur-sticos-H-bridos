"""
plot.py
Funciones para visualización de resultados.
"""

import matplotlib.pyplot as plt

def plot_convergence(history):
    """
    Grafica la evolución del fitness.

    Parámetros:
        history (list): valores de fitness por generación
    """
    plt.plot(history)
    plt.xlabel("Generación")
    plt.ylabel("Distancia")
    plt.title("Convergencia del Algoritmo Genético")
    plt.grid()
    plt.show() 