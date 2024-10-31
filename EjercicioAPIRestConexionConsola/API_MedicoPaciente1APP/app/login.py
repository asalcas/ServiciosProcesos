import token
import requests


def login():
    username = input("User: ")
    password = input("Password: ")
    resultado = requests.post("http://localhost:5050/users/login",
        json ={"username": username, "password": password},
        headers ={"Content-Type": "application/json"},
        token = resultado.json().get("token"))
    return token

def registro():
    username = input("Introduce un nuevo usuario: ")
    password = input("Establece tu contraseña: ")
        json = {"username": username, "password": password},
        return False

# Comprobar en el registro si el usuario existe, y si ya existe el nombre de usuario

for usuario in lista_users:
    if usuario ["username"] == nuevo_usuario:
        return {"error": "usuario ya existe"}, 409