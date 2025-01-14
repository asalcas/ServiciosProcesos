# coding: latin1

from flask import Flask, request, jsonify

# Esto crea una instancia de una aplicación FLASK, que se utilizará para manejar solicitudes web y definir rutas, vistas y comportamientos específicos de la aplicación.
# __name__ es una variable especial de Python que se refiere al nombre de donde está el codigo
app = Flask(__name__)


# BD Provisional
peliculas = [
    {
        "Id": 1,
        "Titulo": "La singular vida de ibelin",
        "Genero": "Documental"
    },
    {
        "Id": 2,
        "Titulo": "Vendetta",
        "Genero": "Accion"
    }
]

series = [
    {
        "Id": 1,
        "Titulo": "Secret Level",
        "Genero": "Accion",
        "Temporadas" : "1",
        "Capitulos" : "15"
    },
    {
        "Id": 2,
        "Titulo": "Juego de Tronos",
        "Genero": "Accion",
        "Temporadas" : "8",
        "Capitulos" : "10"
    }
]


# Ahora definiremos la pagina principal de la api: 'indice'
# Usamos un decorador '@app.route('/')' para indicar de que para nuestra aplicacion la dirección '/' es la base del programa
@app.route('/') 
def indice():
    return 'Hola, esta es la pagina principal, si quieres realizar alguna consulta, escribe en la barra de navegacion "peliculas o series + /"'

#*GET--------------------------------------------------------------------------------------------
#! RUTAS DISTINTOS VERBOS
# @app hace referencia al OBJETO de tipo Flask creado al inicio
@app.get("/peliculas") #? Dentro de los parentesis le indicamos la ruta que se usará para hacer la petición, si buscamos la 'uri + /peliculas' ejecutará esta funcion:
def get_peliculas():
    return (jsonify(peliculas)) 
# Mostrará todos nuestros resultados de 'peliculas' con el verbo GET

# Ahora realizaremos un GET mas preciso, aportando el ID de la película:

@app.get("/peliculas/<int:id>")
def get_peliculasPorID(id):
    for contenido in peliculas:
        if contenido["Id"] == id: #? La 'clave' de Clave valor debe corresponder al 100% con la clave que tenemos en la BD o diccionario
            return contenido, 200
        else: 
            return {"error": "Pelicula no encontrada"}, 404

# De igual forma funciona la ruta base para el GET de 'series'

@app.get("/series")
def get_series():
    return (jsonify(series))


@app.get("/series/<int:id>")
def get_seriesPorID(id):
    for contenido in series:
        if contenido["Id"] == id: #? La 'clave' de Clave valor debe corresponder al 100% con la clave que tenemos en la BD o diccionario
            return contenido, 200
        else: 
            return {"error": "Serie no encontrada"}, 404
        
        
#*PUT/PATCH-------------------------------------------------------------------------------------------        
# Ahora haremos el PUT/PATCH que es lo mismo practicamente: 
# Como tenemos que modificar una pelicula en concreto.
@app.put("/peliculas/<int:id>")
@app.patch("/peliculas/<int:id>")
# Definimos la función correspondiente
def modificarPelicula(id):
    # Se comprueba si la petición que nos ha llegado cumple el formato JSON
    if request.is_json:
        # Creamos una variable donde guardamos el formato JSON, que coincide con un DICCIONARIO
        nuevosDatos = request.get_json()
        # Tenemos que coger de la lista de peliculas, una pelicula en concreto seleccionandola por su 'Id'
        for contenido in peliculas:
            if contenido["Id"] == id:
                # Modifucamos todos los atributos del país con los nuevos valores indicados en el JSON
                for clave in nuevosDatos:
                    contenido[clave] == nuevosDatos[clave]
                    # Devolvemos la película en formato diccionario y el codigo 200 de correcto
                return contenido, 200
    return {"error": "El formato tiene que ser JSON"}, 415
#*--------------------------------------------------------------------------------------------
# Ahora Creamos nuestro 'main' y ahi ejecutamos nuestra API, en el puerto '5050' y en el host '0.0.0.0' 
# Ya no hace falta tocar más el main.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)