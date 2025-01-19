from flask import Blueprint, request
from funcionesRW import leerArchivo,escribirArchivo
import bcrypt
from flask_jwt_extended import create_access_token

usuariosJsonDb = "crud2ApiRefuerzo//api//DB//usuarios.json"

usersBP = Blueprint('usuarios', __name__)

#*POST-----------------------------------------------------------------------

@usersBP.post("/registro")
def registroUsuario():
    usuarios = leerArchivo(usuariosJsonDb)
    if request.is_json:
        # Tomamos la peticion JSON que le hacemos por POSTMAN
        nuevoUsuario = request.get_json()
        # Convertimos la contraseña a un conjunto de bytes
        contra = nuevoUsuario['password'].encode('utf-8')
        # Generamos la sal, que son los caracteres y simbolos que irán dentro de la contraseña
        salt = bcrypt.gensalt()
        # Calculamos el hash y lo convertimos en hexagesimal
        hashPassword = bcrypt.hashpw(contra,salt).hex()
        # Machacamos el campo contraseña del usuario por el hash calculado
        nuevoUsuario['password'] = hashPassword
        # Añadimos el usuario en la lista de usuarios
        # Ahora seria asi: {"username" : "alvaro", "password": "AE234562356"}
        usuarios.append(nuevoUsuario)
        # Reescribimos el fichero
        escribirArchivo(usuarios, usuariosJsonDb)
        # Ahora devolveremos un token que utilizará para hacer llamadas a los métodos que requieran autorización
        token = create_access_token(identity = nuevoUsuario['username'])
        print(usuarios)
        return {'token': token}, 201
    # Si la peticion no es un JSON entonces 'Error'
    return {'Error':'Peticion debe ser JSON'}, 415

# ✅

#*LOGIN(GET)----------------------------------------------------------------------

@usersBP.post('/login')
def loginUsuario():
    # Guardamos en 'listaUsuarios' el contenido de 'usuariosJsonDb'
    listaUsuarios = leerArchivo(usuariosJsonDb)
    # Comprobamos que la petición esté en formato JSON
    if request.is_json:
        # Guardamos la peticion del usuario que va a INICIAR SESION
        usuarioLogin = request.get_json()
        # Guardamos las dos clave que tiene el objeto en el JSON (usuario y contraseña)
        username = usuarioLogin['username']
        password = usuarioLogin['password'].encode('utf-8') 
        # Vamos comprobando el 'username' por cada usuario dentro del JSON
        for usuario in listaUsuarios:
            if usuario['username'] == username: # Cuando encuentre el usuario que corresponde con lo que guardamos en el 'username'
                passwordJSON = usuario['password'] # Asignamos a 'passwordJSON' el valor de la clave 'password' que tenemos en el JSON
                if bcrypt.checkpw(password,bytes.fromhex(passwordJSON)): # Chequeamos que si encriptamos la contraseña que el usuario dió da el mismo resultado del token
                    token = create_access_token(identity = username)# Si es valido, entonces guardamos el token
                    return {'token': token}, 200 # Y lo retornamos
            else:
                {'Error': 'No autorizado'}, 401 # Si no, no escribió su contraseña
        return{'Error':'Usuario no encontrado'}, 404 # No se encontró usuario con ese 'username'
    return{'Error': ' Petición debe ser JSON'}, 415 # La petición no está en el formato correcto


#*GETPOSTMAN------------------------------------------------------------
@usersBP.get('/')
def loginUsuarios():
    # Guardamos en 'listaUsuarios' el contenido de 'usuariosJsonDb'
    listaUsuarios = leerArchivo(usuariosJsonDb)
    # Comprobamos que la petición esté en formato JSON
    if request.is_json:
        # Guardamos la peticion del usuario que va a INICIAR SESION
        usuarioLogin = request.get_json()
        # Guardamos las dos clave que tiene el objeto en el JSON (usuario y contraseña)
        username = usuarioLogin['username']
        password = usuarioLogin['password'].encode('utf-8') 
        # Vamos comprobando el 'username' por cada usuario dentro del JSON
        for usuario in listaUsuarios:
            if usuario['username'] == username: # Cuando encuentre el usuario que corresponde con lo que guardamos en el 'username'
                passwordJSON = usuario['password'] # Asignamos a 'passwordJSON' el valor de la clave 'password' que tenemos en el JSON
                if bcrypt.checkpw(password,bytes.fromhex(passwordJSON)): # Chequeamos que si encriptamos la contraseña que el usuario dió da el mismo resultado del token
                    token = create_access_token(identity = username)# Si es valido, entonces guardamos el token
                    return {'token': token}, 200 # Y lo retornamos
            else:
                {'Error': 'No autorizado'}, 401 # Si no, no escribió su contraseña
        return{'Error':'Usuario no encontrado'}, 404 # No se encontró usuario con ese 'username'
    return{'Error': ' Petición debe ser JSON'}, 415 # La petición no está en el formato correcto

