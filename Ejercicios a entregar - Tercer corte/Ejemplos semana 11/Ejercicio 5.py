# Función que calcula el factorial de un número
def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i  # Multiplicamos acumulando el resultado
    return factorial

try:
    # Pedimos al usuario un número entero positivo
    numero = int(input("Ingrese un número entero positivo: "))

    if numero < 0:
        print("El factorial no está definido para números negativos.")
    else:
        # Llamamos a la función para calcular el factorial
        resultado = calcular_factorial(numero)
        # Mostramos el resultado
        print(f"El factorial de {numero} es: {resultado}")

except ValueError:
    print("Por favor, ingrese un número entero válido.")
