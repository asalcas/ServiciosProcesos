# coding: latin1

from flask import Flask, request, jsonify

# Esto crea una instancia de una aplicación FLASK, que se utilizará para manejar solicitudes web y definir rutas, vistas y comportamientos específicos de la aplicación.
# __name__ es una variable especial de Python que se refiere al nombre de donde está el codigo
app = Flask(__name__)

# Ahora definiremos la pagina principal de la api: 'indice'
# Usamos un decorador '@app.route('/')' para indicar de que para nuestra aplicacion la dirección '/' es la base del programa
@app.route('/') 
def indice():
    return 'Hola, esta es la pagina principal, si quieres realizar alguna consulta, escribe en la barra de navegacion "peliculas o series + /"'

# Ahora Creamos nuestro 'main' y ahi ejecutamos nuestra API, en el puerto '5050' y en el host '0.0.0.0' 
# Ya no hace falta tocar más el main.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)