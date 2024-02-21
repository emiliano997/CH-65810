# Crea una funcion que sirva para Calcular la factorial de un numero hecho en python con documentacion incluida

def factorial(n):
    """Calcula el factorial de un numero.

    Args:
        n (int): El numero a calcular el factorial.

    Returns:
        int: El factorial del numero.
    """
    if n < 0:
        raise ValueError("El numero no puede ser negativo")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Prueba de la funcion
print(factorial(5))
print(factorial.__doc__)
print(factorial.__name__)

# Probar con un numero negativo
try:
    print(factorial(-5))

except ValueError as e:
    print(e)
    