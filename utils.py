"""
utils.py
Funciones auxiliares.
"""

import random

NUM_LOCATIONS = 10

# Generar puntos aleatorios
locations = [
    (
        random.randint(0, 100),
        random.randint(0, 100)
    )
    for _ in range(NUM_LOCATIONS)
]

def calculate_distance(route):
    """
    Distancia total.
    """

    total = 0

    for i in range(len(route) - 1):

        x1, y1 = locations[route[i]]
        x2, y2 = locations[route[i + 1]]

        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        total += distance

    return total

def calculate_time(route):
    """
    Tiempo total estimado.
    """

    distance = calculate_distance(route)

    traffic_factor = 1.2

    return distance * traffic_factor

def calculate_cost(route):
    """
    Costo total estimado.
    """

    distance = calculate_distance(route)

    fuel_cost = 0.5

    return distance * fuel_cost

def fitness(route):
    """
    Fitness multiobjetivo.

    Menor distancia, tiempo y costo
    generan mejor fitness.
    """

    distance = calculate_distance(route)
    time = calculate_time(route)
    cost = calculate_cost(route)

    # Minimización multiobjetivo
    score = 1 / (distance + time + cost)

    return score