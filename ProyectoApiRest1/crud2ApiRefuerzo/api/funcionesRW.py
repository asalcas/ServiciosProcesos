from flask import json

def leerArchivo(rutaLeer):
    with open(rutaLeer,'r') as archivo:
        resultado = json.load(archivo)
    return resultado

def escribirArchivo(contenido, rutaEscribir):
    with open(rutaEscribir,'w') as archivo:
        json.dump(contenido, archivo, indent = 4)
        
        
