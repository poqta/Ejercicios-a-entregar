# Paso 1: Importar modulo datetime
from datetime import datetime

#Paso 2: Solicitar entrada del usuario 
entrada = input ("Ëscribe tu entrada del diario: ") 

#Paso 3: Abrir el archivo en modo de adición ('a')
with open("diario.txt", "a", encoding="utf-8") as archivo:
    #Paso 4: Obtener fecha y hora actual
  fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
  #Escribir la entrada en el archivo 
  archivo.write(f"[{fecha_hora}]\n{entrada}\n\n")
  
#Paso 5: Mostrar mensaje de confirmacion
print ("Entrada guardada correctamente en 'diario.txt'.")
