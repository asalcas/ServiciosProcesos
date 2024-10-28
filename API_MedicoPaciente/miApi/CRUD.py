# Coding: latin1

import json
from pip._vendor import requests






import requests

# DEFINIMOS LAS FUNCIONES DE LA API (GET, POST, PATCH, PUT Y DELETE)
def metodoGET():
    api_url = "https://jsonplaceholder.typicode.com/todos/10" # URL de donde sacaremos la información
    response = requests.get(api_url) # A la variable respuesta le decimos que tiene que obtener la informacion de api_url (.get)
    print("Datos recibidos: ")
    print(response.json()) # Convierte el JSON que nos va a enviar la peticion HTTP a una lista para poder verlo
    print("Código de estado:", response.status_code)

def metodoPATCH(title, completedBoolean):
    api_url = "https://jsonplaceholder.typicode.com/todos/10" # URL de donde actualizaremos la información PARCIALMENTE
    todo = {"title": title, "completed": completedBoolean} # Creamos un DICCIONARIO con los datos que introduzca el usuario (title, y si esta completo)
    response = requests.patch(api_url, json=todo) # ACTUALIZAMOS PARCIALMENTE el registro de la URL, diciendole que DICCIONARIO usar.
    print("Datos actualizados con éxito:")
    print(response.json())  # Convierte el JSON que nos va a enviar la peticion HTTP a una lista para poder verlo
    print(response.status_code) # Para que nos mande por consola el código, para ver si es correcto (201)

def metodoPOST(userID, title, completedBoolean):
    api_url = "https://jsonplaceholder.typicode.com/todos/"# URL donde publicaremos un nuevo REGISTRO
    todo = {"userId": userID, "title": title, "completed": completedBoolean} # Creamos un DICCIONARIO con los datos que introduzca el usuario (userID, title, y si esta completo)
    response = requests.post(api_url, json=todo) # PUBLICAMOS el registro de la URL, diciendole que DICCIONARIO usar.
    print("Publicación creada con éxito:")
    print(response.json())
    print("Código de estado:", response.status_code)

def metodoPUT(userID, title, completedBoolean):
    api_url = "https://jsonplaceholder.typicode.com/todos/10" # URL de donde REEMPLAZAREMOS la información
    todo = {"userId": userID, "title": title, "completed": completedBoolean} # Creamos un DICCIONARIO con los datos que introduzca el usuario (userID, title, y si esta completo)
    response = requests.put(api_url, json=todo) # REEMPLAZAMOS el registro de la URL, diciendole que DICCIONARIO usar.
    print(response.json())
    print(response.status_code)

def metodoDELETE():
    api_url = "https://jsonplaceholder.typicode.com/todos/10" # URL de donde ELIMINAR la información
    response = requests.delete(api_url)
    print(response.json())
    print("Código de estado:", response.status_code)

# Menú principal
def menuOpciones():
    continuar = True
    while continuar:
        print("==================================================")
        print("                    OPCIONES                      ")
        print("==================================================")
        print("1. POST")
        print("2. GET")
        print("3. PATCH")
        print("4. DELETE")
        print("5. SALIDA")

        opcion = int(input("Seleccione una opción de las siguientes: "))

        if opcion < 1 or opcion > 5:
            print("Opción inválida, vuelva a intentarlo.")
        elif opcion == 1:
            # POST: Solicitamos los datos necesarios
            userID = input("Introduce tu identificador: ")
            title = input("Crea un título para esto: ")
            completedBoolean = input("¿Está completado? (1 para sí, 0 para no): ") == "1"
            metodoPOST(userID, title, completedBoolean)
        elif opcion == 2:
            metodoGET()
        elif opcion == 3:
            # PATCH: Solicitamos los datos necesarios
            title = input("Crea un nuevo título para la actualización: ")
            completedBoolean = input("¿Está completado? (1 para sí, 0 para no): ") == "1"
            metodoPATCH(title, completedBoolean)
        elif opcion == 4:
            metodoDELETE()
        elif opcion == 5:
            print("Gracias por utilizar el programa, ¡hasta pronto!")
            continuar = False

# Ejecutamos el menú
menuOpciones()