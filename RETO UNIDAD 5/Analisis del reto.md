# Reto 5 — Análisis y Sustentación
## Objetivo del reto:
**Desarrollar una aplicación en Python que permita al usuario interactuar con archivos .txt y .csv desde un menú sencillo. El programa debe realizar operaciones básicas como contar palabras, reemplazar texto, graficar vocales, mostrar datos, calcular estadísticas y generar gráficos.**

## Estructura del proyecto: 
- RETO.PY: archivo principal con todo el código.
- texto_reto.txt: archivo de texto para pruebas.
- Datos_reto.csv: archivo de datos para análisis.
- Carpeta del proyecto:
C:/Users/juant/Documents/Programacion-2025/prog-2025-2-10am-unidad5-Pablito5852/RETO UNIDAD 5/

## Menú principal: 
El programa inicia con un menú que ofrece 4 opciones:
- Listar archivos en la carpeta del proyecto
- Procesar archivo .txt
- Procesar archivo .csv
- Salir
**Cada opción llama a un submenú o función específica.**

## Funciones para archivos .txt: 
contar_palabras_caracteres()
- Abre el archivo .txt
- Cuenta palabras, caracteres con espacios y sin espacios
- Usa: open(), read(), split(), replace()
reemplazar_palabra()
- Reemplaza una palabra por otra en el texto
- Usa: replace() y vuelve a escribir el archivo
histograma_vocales()
- Cuenta cuántas veces aparece cada vocal
- Grafica con matplotlib.pyplot.bar()

## Funciones para archivos .csv: 
mostrar_csv()
- Solicita al usuario cuántas filas desea ver
- Verifica si ese número existe en el archivo
- Usa: csv.reader(), list(), len()
calcular_estadisticas()
- Pide una columna
- Calcula cantidad, promedio, mínimo y máximo
- Ignora valores no numéricos
- Usa: csv.DictReader(), float(), try-except
graficar_columna()
- Pide una columna
- Grafica dispersión y barras
- Usa: matplotlib.pyplot.scatter() y bar()

## Comandos y funciones utilizadas: 
| Comando / Función         | Explicación breve                                                  |
|---------------------------|---------------------------------------------------------------------|
| `open()`                  | Abre archivos para lectura o escritura                             |
| `read()` / `split()`      | Lee el contenido y separa palabras                                 |
| `replace()`               | Cambia una palabra por otra en un texto                            |
| `csv.reader()`            | Lee archivos `.csv` como listas de filas                           |
| `csv.DictReader()`        | Lee archivos `.csv` como diccionarios por columna                  |
| `float()`                 | Convierte texto a número decimal                                   |
| `try-except`              | Evita errores si el dato no se puede convertir a número            |
| `matplotlib.pyplot.bar()` | Crea gráficos de barras para visualizar datos                      |
| `matplotlib.pyplot.scatter()` | Crea gráficos de dispersión para comparar valores           |
| `os.listdir()`            | Lista todos los archivos en una carpeta                            |
| `input()`                 | Solicita datos al usuario desde la consola                         |
| `print()`                 | Muestra resultados o mensajes en pantalla                          |
| `len()`                   | Calcula la cantidad de elementos en una lista o texto              |
| `min()` / `max()`         | Encuentra el valor mínimo o máximo en una lista de números         |
| `sum()`                   | Suma todos los valores numéricos de una lista                      |

# Validaciones importantes
- Si el usuario pide más filas de las que existen, el programa lo informa.
- Si la columna tiene texto en vez de números, se ignora sin error.
- Si no hay datos válidos, se muestra un mensaje claro.

# Ruta fija del proyecto
Para evitar errores de ubicación, el programa usa esta ruta fija:
ruta_base = "C:/Users/juant/Documents/Programacion-2025/prog-2025-2-10am-unidad5-Pablito5852/RETO UNIDAD 5/"


**Esto garantiza que todos los archivos se encuentren sin importar desde dónde se ejecuta el código.**

# Conclusión
Este reto demuestra el uso práctico de estructuras de control, manejo de archivos, validación de datos y visualización gráfica. El programa es modular, claro y funcional, cumpliendo con todos los requisitos del reto. Está listo para ser sustentado y ampliado en el futuro.
