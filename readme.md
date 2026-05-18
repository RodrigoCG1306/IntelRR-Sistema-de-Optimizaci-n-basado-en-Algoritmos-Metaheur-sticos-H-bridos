# Algoritmos Metaheurísticos

## Proyecto Final – Optimización combinatoria multiobjetivo

* **Alumno:** José Rodrigo Cázares Godoy
* **Carrera:** Ingeniería en Computación (8vo semestre)
* **Profesor:** Mtro. Santo Rubio Pano
* **Universidad:** CUCosta
* **Entrega:** 18 de mayo de 2026

---

## Descripción

Este proyecto implementa un algoritmo metaheurístico híbrido basado en un Algoritmo Genético (GA) combinado con búsqueda local para resolver un problema de optimización multiobjetivo.

El sistema busca optimizar simultáneamente:

* Distancia
* Tiempo
* Costo

Cada solución representa una posible ruta o asignación de recursos. La calidad de cada solución es evaluada mediante una función fitness multiobjetivo.

---

## Metaheurísticas utilizadas

Se combina:

* Algoritmo Genético (GA)
* Búsqueda local

El algoritmo genético explora diferentes soluciones posibles, mientras que la búsqueda local refina las soluciones generadas para mejorar la convergencia.

---

## Tecnologías

* Python
* Matplotlib

---

## Ejecución

```bash
py main.py
