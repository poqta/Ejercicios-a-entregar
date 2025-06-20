#Paso 1: Abrir el archivo productos.csv en modo Lectura
try:
    with open("productos.csv", "r", encoding="utf-8") as archivo:
        print ("Lista de productos:\n")

        #Paso 2: Recorrer el archivo linea por linea
        for linea in archivo:
            #Paso 3: Eliminar salto de linea final
            linea = linea.strip()

            #Paso 4: Separar por comas 
            partes = linea.split(',')

            #Validacion opcional por si alguna lineal no tiene 3 elementos 
            if len(partes) == 3:
                nombre = partes[0]
                precio = partes [1]
                cantidad = partes [2]

                #Paso 5: Imprimir en formato legible
                print (f"Producto: {nombre} | Precio: ${precio} | Stock: {cantidad} unidades")
            else:
                print ("Linea con formato incorrecctos:", linea)

except FileNotFoundError:
    print("El archivo 'productos.csv' no fue encontrado. Asegurate de que exista en la carpeta.")

            
            