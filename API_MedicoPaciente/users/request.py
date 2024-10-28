import bcrypt
from flask import Flask, Blueprint, request
from flask_jwt_extended import create_access_token

from API_MedicoPaciente.app.Pacientes.routes import leerFicherosPacientes

usersBP=Blueprint('usersBP', __name__)

app.config["SECRET_KEY"] = 'patato'



@usersBP.post("/")
def addUser():
   # lista_users = leerFicheros (de nuestro archivo)
        nuevo_usuario = request.get_json()
    if (request.is_json):
        #{"username" : "alvaro", "password": "1234"
        #Recibo un diccionario con "username" y con "password"
        nuevo_usuario = request.get_json()
        # Cojo la contraseña del usuario
        contra = nuevo_usuario["password"].encode('UTF-8')
        sal = bcrypt.gensalt()
        hash = bcrypt.hashpw(contra, sal).hex()
        #almacenamos la contraseña cifrada en el diccionario
        # {"username" : "alvaro", "password": "AE234562356"
        nuevo_usuario["password"] = hash
        #añado el nuevo usuario a la lista
        lista_users.append(nuevo_usuario)

        #lo escribimos en el archivo

        token = create_access_token(identity=nuevo_usuario["username"])
        return {'token': token}, 201
    else:
        return{"error": "JSON incorrecto"},415
