# Crea una función que compruebe si un número es primo o no
# Utiliza la función para mostrar los números primos del 1 al 100
# Agrega una documetación a la función


def esPrimo(n):
    """
    Comprueba si un número es primo o no
    :param n: int
    :return: bool
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(1, 101):
    if esPrimo(i):
        print(i, end=' ')
print()

