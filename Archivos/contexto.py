nombre_archivo = "./Archivos/texto.txt"
# ubicacion = "C:\\Users\\juant\\OneDrive\\Escritorio\\Archivo"
with open(nombre_archivo, "r", encoding = "utf-8") as archivo:
    # Leer todas las lineas dentro de una lista
    lista = archivo.readlines()

#se imprime la lista elemento por elemento
for c in lista:
    print(c)