import csv
Encabezados = ['Nombre', 'Edad', 'Ciudad']
Persona1 = ['Pablo', 17, 'Ingenieria Aeronautica']
Persona2 = ['Federico', 19, 'Derecho']
Persona3 = ['Santiago', 18, 'Trabajo social']
Ubicacion = 'C:\\Users\\juant\\OneDrive\\Escritorio'
Nombre_archivo = "Listas_csv.csv"

with open(Ubicacion + '\\' + Nombre_archivo, 'w',) as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(Encabezados)  # Escribe la fila de encabezados
    escritor.writerow(Persona1)
    escritor.writerow(Persona2)
    escritor.writerow(Persona3)