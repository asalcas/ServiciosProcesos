# Coding: latin-1

#*Imports---------------------------------------------------------------
from flask import request, Blueprint, jsonify
from funcionesRW import leerArchivo, escribirArchivo

peliculasJsonDb = 'C://Users//alvar//Desktop//DAM//ServiciosProcesos//ProyectoApiRest1//crud2ApiRefuerzo//api//DB//peliculas.json' #./api/DB/peliculas.json'
peliculasBP = Blueprint('peliculas', __name__)

#*FuncionAutoincrementar-------------------------------------------------

# Tendremos que crear un metodo que autoincremente el 'Id' leyendo el archivo 'peliculasJsonDb' 
def idAutoincrementadoPeliculas():
    peliculas = leerArchivo(peliculasJsonDb)
    # Coge el 'Id' máximo y le suma +1
    return max(peli["Id"] for peli in peliculas) + 1

#*GET--------------------------------------------------------------------

@peliculasBP.get("/")
def get_peliculasPor():
    # Leemos el archivo 'peliculasJsonDB' y lo guardamos en peliculas
    peliculas = leerArchivo(peliculasJsonDb)
    # Si peliculas NO EXISTE mostramos un error, y si no
    if peliculas == None:
        return{"Error": "No se encontró la pelicula."}, 404
    # Perfesto, codigo 200
    return peliculas, 200

@peliculasBP.get("/<int:id>")
# Como esta peticion necesita de un 'int id' 
def get_peliculasPorID(id):
    # Leemos 'peliculasJsonDb' y lo guardamos en 'peliculas'
    peliculas = leerArchivo(peliculasJsonDb)
    # Comprobamos las pelis del archivo JSON
    for peli in peliculas:
        # Y si el "Id" es == al Id que introducimos entonces lo retornamos
        if peli["Id"] == id:
            return peli, 200
    return{"Error": "No se encontró la pelicula."}, 404

#*POST-----------------------------------------------------------------------

@peliculasBP.post("/")
def add_peliculas():
    # Leemos el archivo 'peliculasJsonDB' y guardamos eso en la variable 'peliculas'
    peliculas = leerArchivo(peliculasJsonDb) #? DUDA, ESTO ES ASÍ O TENDRIA QUE IMPORTARLO?
    # Nos aseguramos de que la request sea en formato 'JSON'
    if request.is_json:
        # Pensemos que 'request' es un formulario, por lo que tendremos que guardar ese formulario hecho dentro de la variable peli
        peli = request.get_json()
        # Le añadimos un 'Id' nuevo
        peli["Id"] = idAutoincrementadoPeliculas()
        # Guardamos la peli al final de las que tenemos en la "tienda"
        peliculas.append(peli)
        # Y escribimos el archivo 'PELICULAS.JSON' 
        escribirArchivo(peliculas)
        return peli, 201
    return {"Error":"Peticion tiene que ser JSON"}, 415

#*PUT/PATCH------------------------------------------------------------------

# Ahora haremos el PUT/PATCH que es lo mismo practicamente: 
# Como tenemos que modificar una pelicula en concreto.
@peliculasBP.put("/<int:id>")
@peliculasBP.patch("/<int:id>")
# Definimos la función correspondiente
def modificarPelicula(id):
    # Se comprueba si la petición que nos ha llegado cumple el formato JSON
    if request.is_json:
        # Leemos el archivo 'peliculasJsonDB' y guardamos eso en la variable 'peliculas'
        peliculas = leerArchivo(peliculasJsonDb) #? DUDA, ESTO ES ASÍ O TENDRIA QUE IMPORTARLO?
        # Creamos una variable donde guardamos el formato JSON, que coincide con un DICCIONARIO
        nuevosDatos = request.get_json()
        # Tenemos que coger de la lista de peliculas, una pelicula en concreto seleccionandola por su 'Id'
        for peli in peliculas: 
            if peli["Id"] == id:
                # Modifucamos todos los atributos del país con los nuevos valores indicados en el JSON
                for clave in nuevosDatos:
                    peli[clave] = nuevosDatos[clave]
                    # Devolvemos la película en formato diccionario y el codigo 200 de correcto
                return peli, 200
    return {"error": "El formato tiene que ser JSON"}, 415

#*DELETE--------------------------------------------------------------------

# A la dirección de peliculas o series se le añade la posibilidad de añadir un ID para eliminar la peli o serie a eliminar
@peliculasBP.delete("/<int:id>")
# Como hay que eliminar una pelicula en cuestion, tenemos que pasar el ID para eliminarlo, pues lo pasaremos por parametros
def eliminar_pelicula(id):
    # Leemos el archivo 'peliculasJsonDB' y guardamos eso en la variable 'peliculas'
    peliculas = leerArchivo(peliculasJsonDb) #? DUDA, ESTO ES ASÍ O TENDRIA QUE IMPORTARLO?
    # Como hay que eliminar una pelicula en concreto, tendremos que buscar en la lista el id de la pelicula que se ha indicado en la petición
    for peli in peliculas: 
        if peli["Id"] == peliculas["Id"]:
            peliculas.remove(peli)
            return "{}", 200 # Si se encuentra el pais:
    return {"Error":"Pelicula no encontrada"}, 404 # Si no se encuentra: 