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
        return False