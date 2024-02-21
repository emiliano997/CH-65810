# Crea una funcion que sirva para Calcular la factorial de un numero hecho en python con documentacion incluida

def factorial(n):
    """Funcion que calcula el factorial de un numero
    
    n int > 0
    returns n!
    """
    # Agrega un try except para que la funcion no se rompa si el usuario ingresa un numero negativo
    if n < 0:
        return 'No se puede calcular el factorial de un numero negativo'
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input('Escribe un numero: '))

print(factorial(n))
