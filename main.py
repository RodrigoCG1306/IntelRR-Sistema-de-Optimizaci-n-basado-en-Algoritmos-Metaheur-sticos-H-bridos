"""
main.py
Ejecución principal.
"""

from ga import run_ga
from plot import plot_results


def main():

    best_solution, history = run_ga(
        pop_size=50,
        generations=100
    )

    print("\nMejor solución encontrada:\n")
    print(best_solution)

    plot_results(history)


if __name__ == "__main__":
    main()