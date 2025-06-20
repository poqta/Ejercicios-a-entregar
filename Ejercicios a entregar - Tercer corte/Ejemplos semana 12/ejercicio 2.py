#Contador de lineas

#Paso 1: Pedir el nombre del archivo al usuario 
nombre_archivo = input("Ingrese el nombre del archivo de texto (ej. datos.txt): ")

try:
    #Paso 2: Abrir el archivo en modo lectura
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        #Paso 3: Leer todas las lineas y contarlas
        lineas = archivo.readlines()
        total_lineas = len(lineas)
    
    #Paso 4: Mostrar el resultadp
    print (f"\nEl archivo '{nombre_archivo}' contiene {total_lineas} lineas(s).")

except FileNotFoundError:
    #Paso 5: Manejar el error si el archivo no existe
    print(f"\nEl archivo ' {nombre_archivo}' no fue encontrado. Verifica el nombre e intenta de nuevo.")
