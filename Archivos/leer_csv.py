import csv

with open('C:\\Users\\juant\\OneDrive\\Escritorio\\variables.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter = ";") #se utiliza el método reader
    encabezados = next(lector)  #Corta toda la primera fila y la guarda en la variable, y sigue asi sucesivamente, se guardan las filas las veces que se ejecuta el next
    print(encabezados[-1])
    Densidad = []
    for fila in lector:
        fila[-1] = fila[-1].replace(',', '.')
        dato = float(fila[-1])          #con el for se itera sobre el objeto para leer
        Densidad.append(dato)
    
    print (Densidad)
    suma = sum(Densidad)
    print(suma)
    promedio = sum(Densidad) / len(Densidad)
    print(promedio)
    
        