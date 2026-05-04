"""
main.py
Archivo principal que ejecuta el proyecto completo.
"""

from utils import generate_cities
from ga import run_ga
from plot import plot_convergence


def main():
    """
    Flujo principal del programa.
    """
    # Generar problema (ciudades)
    cities = generate_cities(10)

    # Ejecutar algoritmo
    best_route, history = run_ga(cities)

    # Mostrar resultado
    print("\nMejor ruta encontrada:")
    print(best_route)

    # Graficar resultados
    plot_convergence(history)


if __name__ == "__main__":
    main()