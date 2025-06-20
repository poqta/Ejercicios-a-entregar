# Función que imprime la tabla de multiplicar del número recibido
def imprimir_tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

try:
    # Pedimos al usuario un número entero
    n = int(input("Ingrese un número entero: "))

    # Llamamos a la función para imprimir la tabla
    imprimir_tabla_multiplicar(n)

except ValueError:
    print("Por favor, ingrese un número entero válido.")
