import os
import csv
import matplotlib.pyplot as plt

ruta = "C:/Users/juant/Documents/Programacion-2025/prog-2025-2-10am-unidad5-Pablito5852/RETO UNIDAD 5/"

def lista_archivos():
    archivos = os.listdir(ruta)
    for archivo in archivos:
        print(archivo)

def contar_palabras_caracteres():
    archivo = input("Nombre del archivo .txt: ")
    with open(ruta + archivo, "r", encoding="utf-8") as f:
        texto = f.read()
        palabras = texto.split()
        total_palabras = len(palabras)
        total_caracteres = len(texto)
        sin_espacios = len(texto.replace(" ", ""))
        print("calabras:", total_palabras)
        print("caracteres con espacios:", total_caracteres)
        print("caracteres sin espacios:", sin_espacios)

def reemplazar_palabra():
    archivo = input("nombre del archivo .txt: ")
    palabra = input("palabra a reemplazar: ")
    Reemplazo = input("nueva palabra: ")
    with open(ruta + archivo, "r", encoding="utf-8") as f:
        texto = f.read()
    nuevo_texto = texto.replace(palabra, Reemplazo)
    with open(ruta + archivo, "w", encoding="utf-8") as f:
        f.write(nuevo_texto)
    print("reemplazado con exito.")

def histograma_vocales():
    archivo = input("Nombre del archivo .txt: ")
    with open(ruta + archivo, "r", encoding="utf-8") as f:
        texto = f.read().lower()
    vocales = ["a", "e", "i", "o", "u"]
    conteo = []
    for v in vocales:
        conteo.append(texto.count(v))
    plt.bar(vocales, conteo, color="green")
    plt.title("Cantidades de cada vocal")
    plt.show()

def mostrar_csv():
    archivo = input("Nombre del archivo .csv: ")
    try:
        cantidad = int(input("Cuantas filas deseas imprimir: "))
    except:
        print("Numero no valido.")
        return
    with open(ruta + archivo, newline="", encoding="utf-8") as f:
        lector = csv.reader(f)
        filas = list(lector)
        total = len(filas)
        if cantidad > total:
            print("El archivo solo tiene estas filas: ",total)
        else:
            for i in range(cantidad):
                print(filas[i])

def calcular_estadisticas():
    archivo = input("Nombre del archivo .csv: ")
    columna = input("Nombre de la columna: ")
    with open(ruta + archivo, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        datos = []
        for fila in lector:
            valor = fila[columna]
            try:
                numero = float(valor)
                datos.append(numero)
            except:
                pass
    if len(datos) == 0:
        print("No se encontraron datos numéricos en esa columna.")
        return
    n = len(datos)
    promedio = sum(datos) / n
    minimo = min(datos)
    maximo = max(datos)
    print("Cantidad:", n)
    print("Promedio:", promedio)
    print("Mínimo:", minimo)
    print("Máximo:", maximo)

def graficar_columna():
    archivo = input("Nombre del archivo .csv: ")
    columna = input("Nombre de la columna: ")
    with open(ruta + archivo, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        datos = []
        for fila in lector:
            valor = fila[columna]
            try:
                numero = float(valor)
                datos.append(numero)
            except:
                pass
    if len(datos) == 0:
        print("Esta columna no contiene datos numericos.")
        return
    plt.scatter(range(len(datos)), datos, color="purple")
    plt.title("Gráfica de dispersión")
    plt.xlabel("Índice")
    plt.ylabel(columna)
    plt.show()
    datos_ordenados = sorted(datos)
    plt.bar(range(len(datos_ordenados)), datos_ordenados, color="blue")
    plt.title("Gráfica de barras")
    plt.xlabel("Índice")
    plt.ylabel(columna)
    plt.show()

def menu_txt():
    while True:
        print("\n1. Contar palabras y caracteres")
        print("2. Reemplazar palabra")
        print("3. Histograma de vocales")
        print("4. Volver")
        opcion = input("Opción: ")
        if opcion == "1":
            contar_palabras_caracteres()
        elif opcion == "2":
            reemplazar_palabra()
        elif opcion == "3":
            histograma_vocales()
        elif opcion == "4":
            break

def menu_csv():
    while True:
        print("\n1. Mostrar filas del archivo")
        print("2. Calcular estadísticas")
        print("3. Graficar columna")
        print("4. Volver")
        opcion = input("Opción: ")
        if opcion == "1":
            mostrar_csv()
        elif opcion == "2":
            calcular_estadisticas()
        elif opcion == "3":
            graficar_columna()
        elif opcion == "4":
            break

def main():
    while True:
        print("\n Menú Principal ")
        print("1. Listar archivos")
        print("2. Procesar archivo .txt")
        print("3. Procesar archivo .csv")
        print("4. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            lista_archivos()
        elif opcion == "2":
            menu_txt()
        elif opcion == "3":
            menu_csv()
        elif opcion == "4":
            break

main()