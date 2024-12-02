


from flask import Flask

from app.Medicos.routes import medicosBP
from app.Pacientes.routes import pacientesBP
from app.Users.routes import usersBP

from flask_jwt_extended import JWTManager




app = Flask(__name__)
app.config["SECRET_KEY"] = 'patato'
jwt = JWTManager(app)


app.register_blueprint(medicosBP, url_prefix='/medicos')
app.register_blueprint(pacientesBP, url_prefix='/pacientes')
app.register_blueprint(usersBP, url_prefix= '/users')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)

