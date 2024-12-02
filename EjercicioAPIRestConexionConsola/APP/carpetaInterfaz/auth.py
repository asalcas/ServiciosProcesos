import token
import requests


def login():
    username = input("User: ")
    password = input("Password: ")
    resultado = requests.get("http://localhost:5050/users/login",
        json ={"username": username, "password": password},
        headers ={"Content-Type": "application/json"})
    if resultado.status_code == 200:
        token = resultado.json().get("token")
        return token
    else:
        print("Error de autenticación:", resultado.text)
        return None

def registro():
    username = input("Introduce un nuevo usuario: ")
    password = input("Establece tu contraseña: ")
    resultado = requests.post("http://localhost:5050/users/register",
        json ={"username": username, "password": password},
        headers ={"Content-Type": "application/json"})
    if resultado.status_code == 200:
        token = resultado.json().get("token")
        return token
    else:
        print("Error de autenticación:", resultado.text)
        return None
