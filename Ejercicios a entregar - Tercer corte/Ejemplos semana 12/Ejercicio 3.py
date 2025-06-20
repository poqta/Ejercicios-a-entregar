



with open ("compras.txt", "w", encoding="utf-8") as archivo: 
    print ("Generador de Lista de Compras")
    print ("Escribe los productos uno por uno. Escribe 'fin' para terminar.\n")

    #Paso 2: Crear un bucle infinito
    while True:
        #Paso 3: Pedir al usuario que ingrese un producto
        producto= input("Producto: ")

        #Paso 4: Verificar si la entrada es "fin"
        if producto.lower() == "fin":
            break

        #Paso 5: Escribir el producto en el archivo
        archivo.write(producto + "\n")
    
#Paso 6: Notificar al usuario
print  ("\n Lista de compras guardada correctamente en 'compras.txt'.")