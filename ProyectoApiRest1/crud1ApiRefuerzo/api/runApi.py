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
    for peli in peliculas:
        if peli["Id"] == id: #? La 'clave' de Clave valor debe corresponder al 100% con la clave que tenemos en la BD o diccionario
            return peli, 200
        else: 
            return {"error": "Pelicula no encontrada"}, 404

# De igual forma funciona la ruta base para el GET de 'series'

@app.get("/series")
def get_series():
    return (jsonify(series))


@app.get("/series/<int:id>")
def get_seriesPorID(id):
    for peli in series:
        if peli["Id"] == id: #? La 'clave' de Clave valor debe corresponder al 100% con la clave que tenemos en la BD o diccionario
            return peli, 200
        else: 
            return {"error": "Serie no encontrada"}, 404
        
        
#*POST.PELICULAS--------------------------------------------------------------------------------------
# Crearemos una funcion que calcule el siguiente ID. Cogiendo el maximo id que encuentre en la lista y le suma +1
def idAutoincrementadoPeliculas():
    return max(peli["Id"] for peli in peliculas) + 1

@app.post("/peliculas")
def add_pelicula():
    # Se comprueba si la petición que nos ha llegado cumple con el formato JSON
    if request.is_json:
        # Creamos una variable donde guardamos el formato JSON
        peli = request.get_json()
        # Le indicamos al diccionario country que su nuevo ID es el que nos devuelve la función _find_next_id()
        peli["Id"] = idAutoincrementadoPeliculas()
        # Añadimos la nueva pelicula
        peliculas.append(peli)
        # Devolve la pelicula en formato diccionario y el codigo 201 para indicar que se ha añadido
        return peli, 201
    return{"error":"Request must be JSON"}, 415

#*POST.SERIES--------------------------------------------------------------------------------------
# Crearemos una funcion que calcule el siguiente ID. Cogiendo el maximo id que encuentre en la lista y le suma +1
def idAutoincrementadoPeliculas():
    return max(serie["Id"] for serie in series) + 1

@app.post("/series")
def add_pelicula():
    # Se comprueba si la petición que nos ha llegado cumple con el formato JSON
    if request.is_json:
        # Creamos una variable donde guardamos el formato JSON
        serie = request.get_json()
        # Le indicamos al diccionario country que su nuevo ID es el que nos devuelve la función _find_next_id()
        serie["Id"] = idAutoincrementadoPeliculas()
        # Añadimos la nueva pelicula
        peliculas.append(serie)
        # Devolve la pelicula en formato diccionario y el codigo 201 para indicar que se ha añadido
        return serie, 201
    return{"error":"Request must be JSON"}, 415

#*PUT/PATCH--------------------------------------------------------------------------------------       
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
        for peli in peliculas:
            if peli["Id"] == id:
                # Modifucamos todos los atributos del país con los nuevos valores indicados en el JSON
                for clave in nuevosDatos:
                    peli[clave] == nuevosDatos[clave]
                    # Devolvemos la película en formato diccionario y el codigo 200 de correcto
                return peli, 200
    return {"error": "El formato tiene que ser JSON"}, 415

#*DELETE--------------------------------------------------------------------------------------

# A la dirección de peliculas o series se le añade la posibilidad de añadir un ID para eliminar la peli o serie a eliminar
@app.delete("/peliculas/<int:id>")
# Como hay que eliminar una pelicula en cuestion, tenemos que pasar el ID para eliminarlo, pues lo pasaremos por parametros
def eliminar_pelicula(id):
    # Como hay que eliminar una pelicula en concreto, tendremos que buscar en la lista el id de la pelicula que se ha indicado en la petición
    for peli in peliculas:
        if peli["Id"] == peliculas["Id"]:
            peliculas.remove(peli)
            return "{}", 200 # Si se encuentra el pais:
    return {"Error":"Pelicula no encontrada"}, 404 # Si no se encuentra: 


#*--------------------------------------------------------------------------------------------
# Ahora Creamos nuestro 'main' y ahi ejecutamos nuestra API, en el puerto '5050' y en el host '0.0.0.0' 
# Ya no hace falta tocar más el main.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)