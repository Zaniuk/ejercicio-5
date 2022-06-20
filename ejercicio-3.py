#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def bisiesto(n):
    if n % 4 == 0: return True 
    else: return False

n = int(input('Ingrese un año \n'))

print(bisiesto(n))