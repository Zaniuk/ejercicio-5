"""
    Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
"""
import math
def area_tria(h, b):
    return (b*h)/2

print(area_tria(12,3))

def area_circ(r):
    return math.pi * (r*r)

print(area_circ(32))