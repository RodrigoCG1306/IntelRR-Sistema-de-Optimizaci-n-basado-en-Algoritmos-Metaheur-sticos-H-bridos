"""
ga.py
Implementación del Algoritmo Genético híbrido para optimización de rutas.
"""

import random
from utils import total_distance


def create_population(size, num_cities):
    """
    Genera la población inicial de soluciones.

    Cada individuo es una permutación de ciudades.

    Parámetros:
        size (int): tamaño de la población
        num_cities (int): número de ciudades

    Retorna:
        list[list]: población inicial
    """
    population = []
    base = list(range(num_cities))

    for _ in range(size):
        individual = base[:]
        random.shuffle(individual)
        population.append(individual)

    return population


def selection(population, cities):
    """
    Selección por torneo (elige el mejor de dos).

    Parámetros:
        population (list): lista de individuos
        cities (list): coordenadas

    Retorna:
        list: individuo seleccionado
    """
    a, b = random.sample(population, 2)
    return a if total_distance(a, cities) < total_distance(b, cities) else b


def crossover(parent1, parent2):
    """
    Cruce ordenado para mantener rutas válidas.

    Parámetros:
        parent1, parent2 (list): padres

    Retorna:
        list: hijo generado
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
    Mutación por intercambio de dos posiciones.

    Parámetros:
        individual (list): solución
    """
    i, j = random.sample(range(len(individual)), 2)
    individual[i], individual[j] = individual[j], individual[i]


def local_search(route, cities):
    """
    Mejora local (hibridación del algoritmo).

    Aplica pequeñas perturbaciones y conserva mejoras.
    Esto convierte el GA en un enfoque híbrido.

    Parámetros:
        route (list): solución inicial
        cities (list): coordenadas

    Retorna:
        list: solución mejorada
    """
    best = route[:]

    for _ in range(10):
        i, j = random.sample(range(len(route)), 2)
        new = best[:]
        new[i], new[j] = new[j], new[i]

        if total_distance(new, cities) < total_distance(best, cities):
            best = new

    return best


def run_ga(cities, pop_size=50, generations=200):
    """
    Ejecuta el algoritmo genético híbrido.

    Parámetros:
        cities (list): coordenadas
        pop_size (int): tamaño de población
        generations (int): número de iteraciones

    Retorna:
        tuple:
            - mejor ruta encontrada
            - historial de fitness
    """
    num_cities = len(cities)
    population = create_population(pop_size, num_cities)

    history = []

    for gen in range(generations):
        new_population = []

        for _ in range(pop_size):
            p1 = selection(population, cities)
            p2 = selection(population, cities)

            child = crossover(p1, p2)

            if random.random() < 0.1:
                mutate(child)

            # 🔥 hibridación
            child = local_search(child, cities)

            new_population.append(child)

        population = new_population

        best = min(population, key=lambda x: total_distance(x, cities))
        best_dist = total_distance(best, cities)

        history.append(best_dist)

        print(f"Gen {gen} -> {best_dist:.2f}")

    return best, history