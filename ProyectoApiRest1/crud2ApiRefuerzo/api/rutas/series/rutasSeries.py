
from flask import Blueprint, jsonify, request
from funcionesRW import leerArchivo, escribirArchivo


seriesJsonDb ='C://Users//alvar//Desktop//DAM//ServiciosProcesos//ProyectoApiRest1//crud2ApiRefuerzo//api//DB//series.json' #./api/DB/peliculas.json'
seriesBP = Blueprint('series',__name__)


#*FuncionAutoincrementar-------------------------------------------------

def idAutoincrementadoSeries():
    series = leerArchivo(seriesJsonDb)
    return max(show["Id"] for show in series) + 1

#*GET--------------------------------------------------------------------


@seriesBP.get("/")
def get_Series():
    series = leerArchivo(seriesJsonDb)
    if series == None:
        return{"Error": "No se encontró la serie."}, 404
    return series, 200

@seriesBP.get("/<int:id>")
def get_SeriePorID(id):
    series = leerArchivo(seriesJsonDb)
    for show in series:
        if show["Id"]== id:
            return show, 200
    return{"Error": "No se encontró la serie."}, 404



#*POST-----------------------------------------------------------------------
@seriesBP.post("/")
def add_serie():
    series = leerArchivo(seriesJsonDb)
    if request.is_json:
        show = request.get_json()
        show["Id"] == idAutoincrementadoSeries
        series.append(series)
        escribirArchivo(series)
        return show, 201
    return {"Error":"Peticion tiene que ser JSON"}, 415