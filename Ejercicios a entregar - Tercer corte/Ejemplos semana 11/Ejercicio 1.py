def calcular_presupuesto(monto):
    # Porcentajes para cada departamento
    recursos_humanos = monto * 0.50
    manufactura = monto * 0.25
    empaquetado = monto * 0.15
    publicidad = monto * 0.10

    # Mostramos los resultados
    print("Distribución del presupuesto:")
    print(f"Recursos Humanos: ${recursos_humanos:.2f}")
    print(f"Manufactura: ${manufactura:.2f}")
    print(f"Empaquetado: ${empaquetado:.2f}")
    print(f"Publicidad: ${publicidad:.2f}")

# Pedimos el monto al usuario
try:
    monto_total = float(input("Ingrese el monto total del presupuesto anual: $"))
    calcular_presupuesto(monto_total)
except ValueError:
    print("Por favor, ingrese un número válido.")
