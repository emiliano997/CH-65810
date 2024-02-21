# Crea una función que compruebe si un número es primo o no

def es_primo(numero):
    """Comprueba si un número es primo o no

    Args:
        numero (int): Número a comprobar

    Returns:
        bool: True si el número es primo, False si no lo es
    """
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Ejemplo de uso:
numero = int(input("Ingrese un número entero positivo mayor que 1: "))

if es_primo(numero):
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo")