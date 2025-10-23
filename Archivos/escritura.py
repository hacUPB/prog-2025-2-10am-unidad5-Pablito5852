Ubicacion = "C:\\Users\\juant\\OneDrive\\Escritorio\\Archivo"
#\ Se usa para comandos de texto
nombre_archivo = "datos2.txt"
modo = "x" #Solo escritura - sobreescribe
fp = open(Ubicacion+"\\"+nombre_archivo, modo,encoding="utf-8")
frase = input("Por favor ingrese su nombre: ")
Edad = int(input("Ingrese su edad: "))
Estatura = float(input("ingrese su estatura: "))
fp.write(frase + "\n")
fp.write(str(Edad) + "\n")
fp.write(str(Estatura) + "\n")
fp.write("\n")
#solicitar una variable entera y una flotante al usuario y la escriben en el archivo

fp.close()