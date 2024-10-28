from flask import Flask

from .Medicos.routes import medicosBP
from .Pacientes.routes import pacientesBP


from flask_jwt_extended import JWTManager




app = Flask(__name__)
app.config ['SECRET_KEY'] = 'nuestra_clave'
jwt = JWTManager(app)


app.register_blueprint(medicosBP, url_prefix='/medicos')
app.register_blueprint(pacientesBP, url_prefix='/pacientes')