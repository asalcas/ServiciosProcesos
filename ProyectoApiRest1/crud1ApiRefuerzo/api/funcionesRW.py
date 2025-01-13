from flask import json

def leerArchivo(rutaLeer):
    with open(rutaLeer,'r') as archivo:
        resultado = json.load(archivo)
    return resultado

def escribirArchivo(resultado, rutaEscribir):
    with open(rutaEscribir,'w') as archivo:
        json.dump(resultado, archivo, indent = 4)