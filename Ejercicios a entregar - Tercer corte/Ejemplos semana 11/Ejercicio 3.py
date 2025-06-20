# Función que calcula el descuento del 10% sobre el salario
def calcular_descuento(salario):
    return salario * 0.10

try:
    # Pedimos la cantidad de empleados
    cantidad = int(input("Ingrese la cantidad de empleados: "))

    # Recorremos cada empleado uno por uno
    for i in range(1, cantidad + 1):
        print(f"\nEmpleado {i}:")
        
        # Pedimos el salario del empleado
        salario = float(input("  Ingrese el salario: $"))
        
        # Calculamos el descuento usando la función
        descuento = calcular_descuento(salario)
        
        # Calculamos el total a pagar luego del descuento
        total_pagar = salario - descuento

        # Mostramos el resultado con dos decimales
        print(f"  Descuento de renta (10%): ${descuento:.2f}")
        print(f"  Total a pagar: ${total_pagar:.2f}")

# En caso de que el usuario escriba algo que no sea número
except ValueError:
    print("Por favor, ingrese números válidos.")
