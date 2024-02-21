def factorial(n):
    """
    Calcula el factorial de un número entero no negativo.

    Args:
    n (int): El número entero del cual se desea calcular el factorial.

    Returns:
    int: El factorial de n.

    Raises:
    ValueError: Si n es un número negativo.

    Examples:
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    """
    try:
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        elif n == 0:
            return 1
        else:
            factorial_result = 1
            for i in range(1, n + 1):
                factorial_result *= i
            return factorial_result
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

# Ejemplos de uso
print(factorial(5))  # Salida: 120
print(factorial(-1))  # Salida: 1
print(factorial(0))  # Salida: 1
