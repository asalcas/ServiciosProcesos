from flask import Flask
from .peliculas.rutasPeliculas import peliculasBP
from .series.rutasSeries import seriesBP

app = Flask(__name__)

# Registramos los Blueprints indicando el nombre del BP y despues el prefijo de la URL
app.register_blueprint(peliculasBP, url_prefix='/peliculas')
app.register_blueprint(seriesBP, url_prefix = '/series')