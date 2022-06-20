"""
    Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
"""
import math
def area_tria(h, b):
    return (b*h)/2

h = int(input("Ingrese la altura del triángulo:\n"))
b = int(input("Ingrese la base del triángulo:\n"))
print("El area del triángulo es: ",area_tria(h,b))

def area_circ(r):
    return math.pi * (r*r)

r = int(input("Ingrese el radio del círculo:\n"))
print("El area del círculo es: ",area_circ(r))