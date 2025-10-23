lista = ["Acho pr", "soldado y profeta", "Esclava", "polvo de hadas", "la quinta sinfonia"]
ubicacion = "C:\\Users\\juant\\OneDrive\\Escritorio\\Archivo"
modo = "w"
# \ se usa para comandos de texto
nombre_archivo = "canciones.txt"
fp = open(ubicacion + "\\" + nombre_archivo, modo,encoding = "utf-8")
#fp.writelines(lista)
for cancion in lista:
    fp.write(cancion + "\n")
fp.close()