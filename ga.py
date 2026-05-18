"""
ga.py
Algoritmo Genético híbrido.
"""

import random

from utils import (
    NUM_LOCATIONS,
    fitness,
    calculate_distance,
    calculate_time,
    calculate_cost
)



def create_population(size):
    """
    Genera población inicial.
    """

    population = []

    base = list(range(NUM_LOCATIONS))

    for _ in range(size):

        individual = base[:]

        random.shuffle(individual)

        population.append(individual)

    return population



def selection(population):
    """
    Selección por torneo.
    """

    a, b = random.sample(population, 2)

    return a if fitness(a) > fitness(b) else b



def crossover(parent1, parent2):
    """
    Cruce ordenado.
    """

    size = len(parent1)

    start, end = sorted(random.sample(range(size), 2))

    child = [-1] * size

    child[start:end] = parent1[start:end]

    pointer = 0

    for gene in parent2:

        if gene not in child:

            while child[pointer] != -1:
                pointer += 1

            child[pointer] = gene

    return child



def mutate(individual):
    """
    Mutación.
    """

    i, j = random.sample(range(len(individual)), 2)

    individual[i], individual[j] = individual[j], individual[i]


def local_search(route):
    """
    Búsqueda local.
    """

    best = route[:]

    best_score = fitness(best)

    for _ in range(10):

        new_route = best[:]

        i, j = random.sample(range(len(route)), 2)

        # intercambiar posiciones
        new_route[i], new_route[j] = (
            new_route[j],
            new_route[i]
        )

        new_score = fitness(new_route)

        # conservar mejora
        if new_score > best_score:

            best = new_route

            best_score = new_score

    return best

def run_ga(pop_size=50, generations=100):
    """
    Ejecuta el algoritmo.
    """

    population = create_population(pop_size)

    history = []

    for gen in range(generations):

        new_population = []

        for _ in range(pop_size):

            p1 = selection(population)
            p2 = selection(population)

            child = crossover(p1, p2)

            if random.random() < 0.1:
                mutate(child)

            # Hibridación
            child = local_search(child)

            new_population.append(child)

        population = new_population

        best = max(population, key=fitness)

        best_fitness = fitness(best)

        history.append(best_fitness)

        print(
            f"Gen {gen} | "
            f"Fitness: {best_fitness:.6f} | "
            f"Distancia: {calculate_distance(best):.2f} | "
            f"Tiempo: {calculate_time(best):.2f} | "
            f"Costo: {calculate_cost(best):.2f}"
        )

    return best, history