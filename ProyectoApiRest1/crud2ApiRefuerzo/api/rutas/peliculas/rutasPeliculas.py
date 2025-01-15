# Coding: latin-1

#*Imports--------------
from flask import app, request, Blueprint, jsonify
from crud2ApiRefuerzo.api.funcionesRW import *
from crud2ApiRefuerzo.api.DB import peliculas


peliculasBP = Blueprint('peliculas',__name__)

#*GET--------------------------------------------------------------------


@peliculasBP.get("/")
def get_peliculasPor():
    peliculas = leerArchivo()
    if peliculas == None:
        return{"Error": "No se encontró la pelicula."}, 404
    return peliculas, 200

@peliculasBP.get("/<int:id>")
def get_peliculasPorID(id):
    peliculas = leerArchivo()
    for peli in peliculas:
        if peli["Id"]== id:
            return peli, 200
    return{"Error": "No se encontró la pelicula."}, 404



#*POST-----------------------------------------------------------------------
def idAutoincrementadoPeliculas():
    return max(peli["Id"] for peli in peliculas) + 1

@peliculasBP.post("/")
def add_peliculas():
    peliculas = leerArchivo()
    if request.is_json:
        peli = request.get_json()
        peli["Id"] == idAutoincrementadoPeliculas
        peliculas.append(peliculas)
        escribirArchivo(peliculas)
        return peli, 201
    return {"Error":"Peticion tiene que ser JSON"}, 415