import json
import bcrypt
from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from pathlib import Path

usersBP=Blueprint('users', __name__)

def leerFicherosUsers():
    path = Path(__file__).with_name('usuarios.json')
    archivo = path.open("r")
    usuarios = json.load(archivo)
    archivo.close()
    return usuarios

def escribirFicherosUsers(usuarios):
    path = Path(__file__).with_name('usuarios.json')
    archivo = path.open("w")
    json.dump(usuarios, archivo)
    archivo.close()

@usersBP.post("/")
def addUser():
    usuarios = leerFicherosUsers()    # lista_users = leerFicheros (de nuestro archivo)
    if (request.is_json): 
        #{"username" : "alvaro", "password": "1234"
        nuevo_usuario = request.get_json()  # Recibo un diccionario con "username" y con "password" del JSON
        contra = nuevo_usuario["password"].encode('UTF-8') # Cojo la contraseña del usuario
        sal = bcrypt.gensalt() # Generamos la SAL
        hashpassword = bcrypt.hashpw(contra, sal).hex() #Calculamos el hash y lo convertimos en hexadecimal
        nuevo_usuario["password"] = hashpassword #Almacenamos la contraseña cifrada en el diccionario
        # Ahora sería así: {"username" : "alvaro", "password": "AE234562356"
        usuarios.append(nuevo_usuario) # Añado el nuevo usuario a la lista
        escribirFicherosUsers(usuarios)

        token = create_access_token(identity=nuevo_usuario["username"])  # Lo escribimos en el archivo
        return {'token': token}, 201
    else:
        return{"error": "JSON incorrecto"},415

@usersBP.get('/')
def inicioSesion():
    usuarios = leerFicherosUsers()
    if(request.is_json):
        buscandoUsuario = request.get_json()
        # Cogemos el usuario y contraseña del JSON
        username = buscandoUsuario['username']
        password = buscandoUsuario["password"].encode('UTF-8')

        for userFile in usuarios:
            if userFile ['username'] == username:
                passwordFile = userFile['password']
                if bcrypt.checkpw(password, bytes.fromhex(passwordFile)):
                    token = create_access_token(identity=username)
                    return {'token': token}, 200
                else: 
                    return {'error': 'No autorizado'}, 401
            return {'Error': 'Usuario no encontrado'}, 404
        return {'Error': 'Debe ser un JSON'}, 415






