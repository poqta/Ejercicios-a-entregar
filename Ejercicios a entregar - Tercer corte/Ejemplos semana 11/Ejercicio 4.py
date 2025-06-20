# Función que calcula el pago total según las horas trabajadas
def calcular_pago(horas_trabajadas):
    # Si trabaja 160 horas o menos, todas se pagan a $6.5
    if horas_trabajadas <= 160:
        pago = horas_trabajadas * 6.5
    else:
        # Las primeras 160 a $6.5
        pago_normal = 160 * 6.5
        # El resto (horas extra) a $7.5
        horas_extra = horas_trabajadas - 160
        pago_extra = horas_extra * 7.5
        # Total a pagar
        pago = pago_normal + pago_extra
    return pago

try:
    # Pedimos al usuario que ingrese el número de horas trabajadas
    horas = float(input("Ingrese el número de horas trabajadas: "))

    # Llamamos a la función para calcular el pago total
    total_pagar = calcular_pago(horas)

    # Mostramos el resultado con dos decimales
    print(f"Total a pagar: ${total_pagar:.2f}")

# En caso de que el usuario escriba algo que no sea un número
except ValueError:
    print("Por favor, ingrese un número válido.")
