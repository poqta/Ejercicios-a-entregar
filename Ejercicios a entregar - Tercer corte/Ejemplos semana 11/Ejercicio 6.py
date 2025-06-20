import math  # Importamos la librería para usar el valor de pi

# Función que calcula el área de un círculo dado su radio
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2  # π * radio al cuadrado
    return area

try:
    # Pedimos al usuario que ingrese el radio
    radio = float(input("Ingrese el radio del círculo: "))

    if radio < 0:
        print("El radio no puede ser negativo.")
    else:
        # Llamamos a la función para calcular el área
        area = calcular_area_circulo(radio)
        # Mostramos el resultado con 2 decimales
        print(f"El área del círculo con radio {radio} es: {area:.2f}")

except ValueError:
    print("Por favor, ingrese un número válido.")
