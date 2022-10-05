try:
    entrada = input("ingrese el archivo: ")
    archivo = open(entrada,"r",encoding ="Utf-8")
    for linea in archivo:
        print(linea.upper())
except:
    print("error. archivo no existente")
