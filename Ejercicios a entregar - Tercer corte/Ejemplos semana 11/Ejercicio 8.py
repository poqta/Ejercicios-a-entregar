def calcular_importe_final(importe):
    # Aplicamos los descuentos según el importe
    if importe > 500:
        descuento = 0.12   # Descuento del 12% para más de 500 €
    elif importe > 300:
        descuento = 0.05   # Descuento del 5% para más de 300 €
    else:
        descuento = 0.0    # Sin descuento

    # Calculamos el importe final restando el descuento
    importe_final = importe * (1 - descuento)
    return importe_final

try:
    # Pedimos al usuario el importe de la compra
    importe_compra = float(input("Ingrese el importe de la compra en euros: €"))

    if importe_compra < 0:
        print("El importe no puede ser negativo.")
    else:
        # Calculamos el importe a pagar usando la función
        total_pagar = calcular_importe_final(importe_compra)
        print(f"El importe final a pagar es: €{total_pagar:.2f}")

except ValueError:
    print("Por favor, ingrese un número válido.")
