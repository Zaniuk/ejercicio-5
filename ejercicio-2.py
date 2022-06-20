# Escribe una función que pueda decirte si un número (número entero) es primo o no.

def primo(n):
    res = []
    for i in range(1, n +1):
        if(n % i == 0):
            res.append(i)
    return len(res) == 2


n = int(input("Por favor inserte un numbero \n"))

print(primo(n))