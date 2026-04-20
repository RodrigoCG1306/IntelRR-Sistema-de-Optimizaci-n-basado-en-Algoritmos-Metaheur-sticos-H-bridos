"""
utils.py
Funciones auxiliares para generación de ciudades y cálculo de distancias.
"""

import random
import math

def generate_cities(n):
    """
    Genera una lista de ciudades con coordenadas aleatorias.

    Parámetros:
        n (int): número de ciudades

    Retorna:
        list[tuple]: lista de coordenadas (x, y)
    """
    return [(random.randint(0, 100), random.randint(0, 100)) for _ in range(n)]


def distance(a, b):
    """
    Calcula la distancia euclidiana entre dos puntos.

    Parámetros:
        a (tuple): punto (x, y)
        b (tuple): punto (x, y)

    Retorna:
        float: distancia entre los puntos
    """
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def total_distance(route, cities):
    """
    Calcula la distancia total de una ruta (fitness).

    Parámetros:
        route (list): orden de visita de las ciudades
        cities (list): lista de coordenadas

    Retorna:
        float: distancia total del recorrido
    """
    dist = 0
    for i in range(len(route)):
        dist += distance(
            cities[route[i]],
            cities[route[(i+1) % len(route)]
        ])
    return dist