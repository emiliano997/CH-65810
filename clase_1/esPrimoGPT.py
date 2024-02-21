def es_primo(numero):
    
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Ejemplo de uso:
numero = int(input("Ingrese un número entero positivo mayor que 1: "))

if es_primo(numero):
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo")
