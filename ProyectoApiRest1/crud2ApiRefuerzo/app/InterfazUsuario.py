# Coding: latin-1
import requests
import time

def crudMain():
    
    print("=========================================================")
    print("==               ¿Que quieres hacer?                   ==")
    print("=========================================================")
    print("1. Iniciar Sesión")
    print("2. Registrar un nuevo usuario")
    
    respuestaUsuario = input("Tu respuesta ")
    
    if (respuestaUsuario == "1"):
        token = loginUsuario()
        # main
    elif(respuestaUsuario == "2"):
        crearUsuario()
        token = loginUsuario()
        # main
    if not token:
        print("Inicio de sesión incorrecto. Saliendo del programa.")
        return
        
    print ("haciendo mas cosas")
    
    print("=========================================================")
    print("==               ¿Que quieres hacer?                   ==")
    print("=========================================================")
    print("1. GET Peliculas")
    print("2. GET Peliculas por ID")
    print("3. PATCH/PUT Peliculas")
    print("4. DELETE Pelicula")
    respuestaUsuario = input("Tu respuesta: ")
    
    if respuestaUsuario == "1":
        getPeliculasAPP(token)
        
    elif respuestaUsuario == "2":
        idPelicula= input("Introduce el Id de la pelicula que quieres ver: ")
        getPeliculasPorIDAPP(token, idPelicula)
        
    elif respuestaUsuario == "3":
        idPelicula= input("Introduce el Id de la pelicula que quieres modificar: ")
        getPeliculasPorIDAPP(token,idPelicula)
        time.sleep(2)
        titulo = input("Introduzca la modificación en el Título: ")
        genero = input("Introduzca la modificación en el Género: ")
        modificarPelicula(token, idPelicula, titulo, genero)
    elif respuestaUsuario == "4":
        idPelicula= input("Introduce el Id de la pelicula que quieres eliminar: ")
        getPeliculasPorIDAPP(token,idPelicula)
        print("¿Es esta la pelicula que quieres eliminar?")
        respuesta = (input("(Y/N):")).lower()
        
        if (respuesta == 'y'):
            borrarPelicula(token,idPelicula)
            print("Pelicula borrada con exito")
            
        elif (respuesta == 'n'):
            print("Se ha cancelado el borrado.")
        else: 
            print("Has introducido una respuesta erronea finalizando el programa.")
    
# Desde la aplicación haremos un login
def loginUsuario():
    # Introducimos los datos usuario y contraseña
    username = input("Usuario: ")
    password = input("Contraseña: ")
    # 'Resultado' hace lo que haria POSTMAN, coge la URL y le manda un JSON con las claves y valores correspondientes:  "username": username, "password": password
    # Que son las variables recogidas anteriormente.
    resultado = requests.post("http://localhost:5050/usuarios/login", json={"username": username, "password": password}, headers={"Content-Type": "application/json"})
    if resultado.status_code == 200: # Si la petición se realiza correctamente.
        token = resultado.json().get("token") # Recogemos en la variable TOKEN el resultado de la petición (que es el token de inicio de sesión)
        print(f"Has iniciado sesión correctamente: {username}") # Para ver que todo funciona correctamente mandamos un mensaje de Éxito.
        return token
    else: 
        print("Error de autenticación:", resultado.text)
        return None

def crearUsuario():
    # Como creemos crear un nuevo usuario, tendremos que guardar el usuario y contraseña en dos nuevas variables: 'username', 'password'
    username = input("Nuevo usuario: ")
    password = input("Nueva contraseña: ")
    # Hacemos la petición que haria POSTMAN: Una llamada a la URL en formato JSON con las claves y valores correspondientes:  "username": username, "password": password
    resultado = requests.post("http://localhost:5050/usuarios/registro", json={"username": username, "password": password}, headers={"Content-Type": "application/json"})
    print("Se ha creado un nuevo usuario con exito" + resultado.text)
    
def getPeliculasAPP(token):
    try:
        respuesta = requests.get(
            "http://localhost:5050/peliculas",
            headers={"Authorization": f"Bearer {token}"}
        )
        if respuesta.status_code == 200:
            print("Lista de Peliculas:", respuesta.json())
        else:
            print("Error al obtener las Peliculas:", respuesta.text + "\n")
    except Exception as e:
        print("Error en la solicitud GET:", e + "\n")
    
    
    
def getPeliculasPorIDAPP(token, peliculaID):
    try:
        peticion = requests.get(
            f"http://localhost:5050/peliculas/{peliculaID}",
            headers={"Authorization": f"Bearer {token}"}
        )
        if peticion.status_code == 200:
            print("\nLista de editoriales:", peticion.json())
        else:
            print("Error al obtener las editoriales:", peticion.text + "\n")
    except Exception as e:
        print("Error en la solicitud GET:", e + "\n") 
    
    
def modificarPelicula(token, idPelicula, titulo, genero):
    try:
        peticion = requests.put(  # Cambié patch a put para actualizar la editorial completa
            f"http://localhost:5050/peliculas/{idPelicula}",
            json={"Titulo": titulo, "Genero": genero},
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        )
        if peticion.status_code == 200:
            print("Pelicula modificada:", peticion.json())
        else:
            print("Error al modificar la pelicula:", peticion.text + "\n")
    except Exception as e:
        print("Error en la solicitud PUT/PATCH:", e + "\n")
    
    
    
def borrarPelicula(token, idPelicula):
    try:
        peticion = requests.delete(
            f"http://localhost:5050/peliculas/{idPelicula}",
            headers={"Authorization": f"Bearer {token}"}
        )
        if peticion.status_code == 200:
            print(f"Pelicula {idPelicula} eliminada con éxito.")
        else:
            print("Error al eliminar la pelicula:", peticion.text + "\n")
    except Exception as e:
        print("Error en la solicitud DELETE:", e + "\n")
        
        
if __name__ == "__main__":
    crudMain()
    
    