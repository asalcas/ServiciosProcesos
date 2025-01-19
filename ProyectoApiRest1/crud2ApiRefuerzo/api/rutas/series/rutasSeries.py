
from flask import Blueprint, jsonify, request
from funcionesRW import leerArchivo, escribirArchivo

seriesJsonDb ='crud2ApiRefuerzo//api//DB//series.json' #! Recuerda que la ruta va DESDE DONDE ESTAS EJECUTANDO EL PROGRAMA
# PS C:\Users\alvar\Desktop\DAM\ServiciosProcesos\ProyectoApiRest1> lo que seria siguiente es 'seriesJsonDb'
seriesBP = Blueprint('series',__name__)


#*FuncionAutoincrementar-------------------------------------------------

# Es una función que lee el archivo 'series.json'
def idAutoincrementadoSeries():
    series = leerArchivo(seriesJsonDb)
    # selecciona el mayor y sumandole 1 al archivo nuevo.
    return max(show["Id"] for show in series) + 1

# ✅

#*GET--------------------------------------------------------------------

@seriesBP.get("/")
def get_Series():
    # Leemos el archivo y lo guardamos en la variable serie
    series = leerArchivo(seriesJsonDb)
    # Si serie es None o sea, vacío. Entonces mandamos su mensaje correspondiente y su codigo: 404
    if series == None:
        return{"Error": "No se encontró la serie."}, 404
    return series, 200 # Si no todo habrá sido correcto

@seriesBP.get("/<int:id>")
# Como estamos buscando un elemento en concreto, haremos la búsqueda por su id, por lo que lo pasaremos por parámetros
def get_SeriePorID(id):
    # Leemos el archivo y almacenamos su valor en 'series'
    series = leerArchivo(seriesJsonDb)
    # Recorremos todo el Json 
    for show in series: 
        # Y cuando el 'Id' de un elemento concuerde con el id que le damos en la Peticion 
        if show["Id"]== id:
            return show, 200 # Entonces peticion correcta 200
    return{"Error": "No se encontró la serie."}, 404 

#✅

#*POST-----------------------------------------------------------------------

# Para hacer una peticion Post, primero tenemos que abrir el archivo y guardarlo 
@seriesBP.post("/")
def add_serie():
    series = leerArchivo(seriesJsonDb)
    # Despues le ponemos la condicion a la peticion de si es Json
    if request.is_json:
        show = request.get_json() # guardamos la peticion en 'show'
        show["Id"] = idAutoincrementadoSeries() # Le asignamos un 'Id' autoincrementado
        series.append(show) # Y lo añadimos al final del archivo 'series.json'
        escribirArchivo(series, seriesJsonDb) # Por ultimo machacamos el archivo 'series.json'
        return show, 201 # Si todo es correcto
    return {"Error":"Peticion tiene que ser JSON"}, 415

#✅

#*PUT/PATCH-----------------------------------------------------------------

@seriesBP.put("/<int:id>")
@seriesBP.patch("/<int:id>")
# Para modificar un registro, tendremos que seleccionarlos por el 'Id'
def updateSerie(id):
    # Nos aseguramos de que su petición sea Json
    if request.is_json:
        # Si es asi, leemos y guardamos el contenido en series
        series = leerArchivo(seriesJsonDb)
        # Guardaremos la peticion en serie modificar
        serieModificar = request.get_json()
        # Por cada elemento dentro del archivo 'seriesJsonDb'
        for serie in series:
            # Vamos comparando el campo 'Id'
            if serie["Id"] == id:
                # Y vamos asignandole un valor a cada clave dentro del registro(Clave: valor)
                for clave in serieModificar:
                    serie[clave] = serieModificar[clave]
                    # Machacamos el archivo Json
                escribirArchivo(series, seriesJsonDb) #! Aqui he tenido un problema, Cuando elijamos que archivo escribir, cuidado con que escribimos
                #! sin querer escribí 'serie' en vez de 'series' y machaque el archivo solo con el elemento a updatear.
                return serie, 200 # Success
            return {"Error":"Serie no encontrada"}, 404
    return {"Error":"Peticion tiene que ser JSON"}, 415

#✅

#*DELETE-------------------------------------------------------------------

@seriesBP.delete("/<int:id>")
# Como tenemos que seleccionar que 'Id' eliminar, lo pasamos por parametros
def eliminar_serie(id):
    # Guardamos el contenido de 'SeriesJsonDb' dentro de 'series'
    series = leerArchivo(seriesJsonDb)
    # Recorremos el archivo y cuando...
    for serie in series:
        # Corresponda el valor de la clave 'Id' con el 'id' pasado por parametros
        if serie["Id"] == id:
            # Eliminamos ese objeto
            series.remove(serie)
            # Y machacamos el archivo 'series.json'
            escribirArchivo(series, seriesJsonDb)
            return series, 200
    return {"Error": "Serie no encontrada"}, 404

#✅
