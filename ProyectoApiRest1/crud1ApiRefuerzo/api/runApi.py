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


#! RUTAS DISTINTOS VERBOS
# @app hace referencia al OBJETO de tipo Flask creado al inicio
@app.get("/peliculas") #? Dentro de los parentesis le indicamos la ruta que se usará para hacer la petición, si buscamos la 'uri + /peliculas' ejecutará esta funcion:
def get_peliculas():
    return(jsonify(peliculas))


# Ahora Creamos nuestro 'main' y ahi ejecutamos nuestra API, en el puerto '5050' y en el host '0.0.0.0' 
# Ya no hace falta tocar más el main.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)