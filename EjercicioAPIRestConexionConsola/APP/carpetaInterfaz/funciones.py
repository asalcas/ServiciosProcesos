#coding: latin1

from flask import jsonify
import requests

#MEDICO
def getMedico():
    api_url = "https://jsonplaceholder.typicode.com/todos/10" # URL de donde sacaremos la información
    response = requests.get(api_url) # A la variable respuesta le decimos que tiene que obtener la informacion de api_url (.get)
    print("Datos recibidos: ")
    print(response.json()) # Convierte el JSON que nos va a enviar la peticion HTTP a una lista para poder verlo
    print("Código de estado:", response.status_code)


def postMedico(userID,title,completedBoolean):
    api_url = "https://jsonplaceholder.typicode.com/todos/"# URL donde publicaremos un nuevo REGISTRO
    todo = {"userId": userID, "title": title, "completed": completedBoolean} # Creamos un DICCIONARIO con los datos que introduzca el usuario (userID, title, y si esta completo)
    response = requests.post(api_url, json=todo) # PUBLICAMOS el registro de la URL, diciendole que DICCIONARIO usar.
    print("Publicación creada con éxito:")
    print(response.json())
    print("Código de estado:", response.status_code)
    
def patchMedico(title, completedBoolean):
    api_url = "https://jsonplaceholder.typicode.com/todos/10" # URL de donde actualizaremos la información PARCIALMENTE
    todo = {"title": title, "completed": completedBoolean} # Creamos un DICCIONARIO con los datos que introduzca el usuario (title, y si esta completo)
    response = requests.patch(api_url, json=todo) # ACTUALIZAMOS PARCIALMENTE el registro de la URL, diciendole que DICCIONARIO usar.
    print("Datos actualizados con éxito:")
    print(response.json())  # Convierte el JSON que nos va a enviar la peticion HTTP a una lista para poder verlo
    print(response.status_code) # Para que nos mande por consola el código, para ver si es correcto (201)
    
def deleteMedico():
    api_url = "https://jsonplaceholder.typicode.com/todos/10" # URL de donde ELIMINAR la información
    response = requests.delete(api_url)
    print(response.json())
    print("Código de estado:", response.status_code)
    
#PACIENTE

def getPaciente():
    api_url = "https://jsonplaceholder.typicode.com/todos/10" # URL de donde sacaremos la información
    response = requests.get(api_url) # A la variable respuesta le decimos que tiene que obtener la informacion de api_url (.get)
    print("Datos recibidos: ")
    print(response.json()) # Convierte el JSON que nos va a enviar la peticion HTTP a una lista para poder verlo
    print("Código de estado:", response.status_code)
    
def postPaciente():
    api_url = "https://jsonplaceholder.typicode.com/todos/"# URL donde publicaremos un nuevo REGISTRO
    todo = {"userId": userID, "title": title, "completed": completedBoolean} # Creamos un DICCIONARIO con los datos que introduzca el usuario (userID, title, y si esta completo)
    response = requests.post(api_url, json=todo) # PUBLICAMOS el registro de la URL, diciendole que DICCIONARIO usar.
    print("Publicación creada con éxito:")
    print(response.json())
    print("Código de estado:", response.status_code)
    
def patchPaciente(title, completedBoolean):
    api_url = "https://jsonplaceholder.typicode.com/todos/10" # URL de donde actualizaremos la información PARCIALMENTE
    todo = {"title": title, "completed": completedBoolean} # Creamos un DICCIONARIO con los datos que introduzca el usuario (title, y si esta completo)
    response = requests.patch(api_url, json=todo) # ACTUALIZAMOS PARCIALMENTE el registro de la URL, diciendole que DICCIONARIO usar.
    print("Datos actualizados con éxito:")
    print(response.json())  # Convierte el JSON que nos va a enviar la peticion HTTP a una lista para poder verlo
    print(response.status_code) # Para que nos mande por consola el código, para ver si es correcto (201)
    
def deletePaciente():
    api_url = "https://jsonplaceholder.typicode.com/todos/10" # URL de donde ELIMINAR la información
    response = requests.delete(api_url)
    print(response.json())
    print("Código de estado:", response.status_code)
    
    