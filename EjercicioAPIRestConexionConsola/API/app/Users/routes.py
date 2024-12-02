import json
import bcrypt
from flask import Blueprint, jsonify, request

from flask_jwt_extended import create_access_token
from pathlib import Path

usersBP=Blueprint('users', __name__)

def leerFicherosUsers():
    path = Path(__file__).with_name('C:\\Users\\alvar\\Desktop\\DAM\\ServiciosProcesos\\EjercicioAPIRestConexionConsola\\API\\DB\\usuarios.json') # PON LA DEL ORDENADOR DEL INSTITUTO CARAJO
    archivo = path.open("r")
    usuarios = json.load(archivo)
    archivo.close()
    return usuarios

def escribirFicherosUsers(usuarios):
    path = Path(__file__).with_name('C:\\Users\\alvar\\Desktop\\DAM\\ServiciosProcesos\\EjercicioAPIRestConexionConsola\\API\\DB\\usuarios.json')
    archivo = path.open("w")
    json.dump(usuarios, archivo)
    archivo.close()

@usersBP.post("/register")
def addUser():
    usuarios = leerFicherosUsers()    # lista_users = leerFicheros (de nuestro archivo)
    if (request.is_json): 
        

        # Comprobar en el registro si el usuario existe, y si ya existe el nombre de usuario
        for usuario in usuarios:
            if usuario ["username"] == nuevo_usuario:
                return {"error": "usuario ya existe"}, 409
        
        
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

@usersBP.route('/login', methods=['POST'])
def login_usuario():
    users = leerFicherosUsers()  # Cargar usuarios desde el archivo
    user_data = request.get_json()
    
    # Verificamos que se haya proporcionado un nombre de usuario y una contraseña
    if 'username' not in user_data or 'password' not in user_data:
        return jsonify({"error": "Usuario y contraseña son requeridos"}), 400

    username = user_data['username']
    password_input = user_data['password'].encode('utf-8')

    # Buscamos el usuario en la lista
    for user in users:
        if user['username'] == username:
            # El hash almacenado está en hexadecimal, lo convertimos a bytes
            password_stored = bytes.fromhex(user['password'])
            # Verificamos la contraseña
            if bcrypt.checkpw(password_input, password_stored):
                token = create_access_token(identity=username)
                return jsonify({"token": token}), 200
            else:
                return jsonify({"error": "Contraseña incorrecta"}), 401

    # Si no encontramos el usuario
    return jsonify({"error": "Usuario no encontrado"}), 404




#IMPORTS 

