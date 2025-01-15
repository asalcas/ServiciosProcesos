
from flask import Blueprint, jsonify, request
from api.funcionesRW import *
from crud2ApiRefuerzo.api.DB import series


seriesBP = Blueprint('series',__name__)

#*GET--------------------------------------------------------------------


@seriesBP.get("/")
def get_Series():
    series = leerArchivo()
    if series == None:
        return{"Error": "No se encontró la serie."}, 404
    return series, 200

@seriesBP.get("/<int:id>")
def get_SeriePorID(id):
    series = leerArchivo()
    for show in series:
        if show["Id"]== id:
            return show, 200
    return{"Error": "No se encontró la serie."}, 404



#*POST-----------------------------------------------------------------------
def idAutoincrementadoSeries():
    return max(show["Id"] for show in series) + 1

@seriesBP.post("/")
def add_serie():
    series = leerArchivo()
    if request.is_json:
        show = request.get_json()
        show["Id"] == idAutoincrementadoSeries
        series.append(series)
        escribirArchivo(series)
        return show, 201
    return {"Error":"Peticion tiene que ser JSON"}, 415