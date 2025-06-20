# Función que recibe tres números y devuelve el menor
def encontrar_menor(a, b, c):
    menor = min(a, b, c)  # Usamos la función min para encontrar el menor
    return menor

try:
    # Pedimos tres números reales al usuario
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))

    # Llamamos a la función para encontrar el menor
    menor_valor = encontrar_menor(num1, num2, num3)

    # Mostramos el resultado
    print(f"El menor de los tres números es: {menor_valor}")

except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
