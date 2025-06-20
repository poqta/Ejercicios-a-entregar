# Función que calcula el 10% de comisión sobre el total de las tres ventas
def calcular_comision(venta1, venta2, venta3):
    total_ventas = venta1 + venta2 + venta3        # Sumamos las tres ventas
    comision = total_ventas * 0.10                 # Calculamos el 10% de comisión
    return comision                                # Devolvemos la comisión

try:
    # Pedimos al usuario la cantidad de vendedores
    n = int(input("Ingrese la cantidad de vendedores: "))

    # Recorremos cada vendedor uno por uno
    for i in range(1, n + 1):
        print(f"\nVendedor {i}:")

        # Pedimos el sueldo base del vendedor
        sueldo_base = float(input("  Ingrese el sueldo base: $"))

        # Pedimos los montos de las tres ventas
        venta1 = float(input("  Ingrese el monto de la primera venta: $"))
        venta2 = float(input("  Ingrese el monto de la segunda venta: $"))
        venta3 = float(input("  Ingrese el monto de la tercera venta: $"))

        # Llamamos a la función para calcular la comisión
        comision = calcular_comision(venta1, venta2, venta3)

        # Sumamos el sueldo base con la comisión para obtener el pago total
        total_pago = sueldo_base + comision

        # Mostramos los resultados con dos decimales
        print(f"  Comisión por ventas: ${comision:.2f}")
        print(f"  Pago total de la semana: ${total_pago:.2f}")

# En caso de que se ingrese un valor no numérico
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
