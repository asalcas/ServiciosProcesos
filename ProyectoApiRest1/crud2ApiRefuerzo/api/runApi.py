from flask import Flask
from rutas.peliculas.rutasPeliculas import peliculasBP
from rutas.series.rutasSeries import seriesBP
from rutas.usuarios.rutasUsuario import usersBP
from flask_jwt_extended import JWTManager # Cuidado, para esto tienes que ejecutar en la terminal el siguiente código:

# 1º python -m pip install Flask-JWT-Extended
# 2º python -m pip install bcrypt

# Ten en cuenta que al crear un nuevo .venv tienes que ejecutar el entorno virtual para poder instalar dentro de la carpeta todo eso.
# Pulsas: 'Cntrol + Shift + P'
# Escribes: "Python: Create Enviroment"
# Y entonces ejecutas lo anterior

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345elmejor' # Nuestra contraseña
jwt = JWTManager(app)

# Registramos los Blueprints indicando el nombre del BP y despues el prefijo de la URL
app.register_blueprint(peliculasBP, url_prefix='/peliculas')
app.register_blueprint(seriesBP, url_prefix = '/series')
app.register_blueprint(usersBP, url_prefix = '/usuarios')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)
    
    # Otros errores que he tenido. 
    # - En los Json fijarse de que tenemos [{},{}] sin los [] da error siempre.
    # - Si tenemos json en los que medimos por id siempre tenemos que tener 1 como mínimo en el archivo, sino no funcionará y dará pete.