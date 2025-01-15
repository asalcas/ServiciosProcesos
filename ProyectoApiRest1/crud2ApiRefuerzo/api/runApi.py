from flask import Flask
from rutas.peliculas.rutasPeliculas import peliculasBP
from rutas.series.rutasSeries import seriesBP

app = Flask(__name__)

# Registramos los Blueprints indicando el nombre del BP y despues el prefijo de la URL
app.register_blueprint(peliculasBP, url_prefix='/peliculas')
app.register_blueprint(seriesBP, url_prefix = '/series')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)