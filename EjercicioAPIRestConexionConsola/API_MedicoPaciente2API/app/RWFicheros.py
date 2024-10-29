from flask import json


def leerFicherosMedicos():
    archivo = open("DB/medicos.json", "r")
    Medicos = json.load(archivo)
    archivo.close()
    return Medicos

def escribirFicherosMedicos(Medicos):
    archivo = open("DB/medicos.json", "w")
    json.dump(Medicos, archivo)
    archivo.close()
