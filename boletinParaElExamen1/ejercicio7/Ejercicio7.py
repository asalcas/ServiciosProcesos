
from multiprocessing import Process, Queue



def leerNumFichero(cola: Queue): # Creamos una función para leer los archivos
    with open("ejercicio7/numerosEjercicio7.txt", "r") as archivo: # Abrimos el archivo "ejercicio7/numerosEjercicio7.txt" con permisos de
                                                                    # lectura con el alias de "archivo"
        for linea in archivo.readlines(): #  Por cada linea en "archivo" 
            idProceso, num1, num2 = map(int, linea.strip().split()) #! Sacamos los datos de la linea (que estaban en una tupla) a sus variables correspondientes
            # linea = 1 1 7\n
            # linea.strip() = 1 1 7
            # linea.split() = ["1", "1", "7"]
            # idProceso = 1
            # num1 = 1
            # num2 = 7
            cola.put((idProceso, num1, num2)) # Pasamos el valor de todas las variables a la cola
            print(f"Para el proceso {idProceso} se han enviado los numeros: {num1} y {num2}") # Hacemos print aqui para ver por donde vamos y si hay errores o no
        cola.put(None) # Si no hay mas elementos en archivo, entonces pasamos None para que se pause la ejecución.
        
def sumarTodo(cola: Queue): # Creamos una función que reciba los datos de la cola, que lleva la información de: "ejercicio7/numerosEjercicio7.txt" 
    numeros = cola.get() # Recibimos los datos de la cola
    suma = 0
    while numeros is not None: # Mientras que numero (que es lo que recibimos por la cola) NO sea None (null)
        idProceso, num1, num2 = numeros # Desempaquetamos los datos
        if num1 > num2: # Comprobamos el orden de los numeros
            num1, num2 = num2, num1 # Si num1 es mayor a num2, entonces cambiamos el orden
        suma = sum(range(num1, num2 + 1)) # Sumamos todo lo que esté entre num1 y num2 incluidos
        print(f"El proceso {idProceso}: El resultado de la suma de todos los numeros entre {num1} y {num2} son: {suma}")
        numeros = cola.get() # Pasamos al siguiente elemento de la cola.

if __name__ == "__main__":
    cola = Queue() # Determinamos que se conectarán los procesos por una Cola
    p1 = Process(target=leerNumFichero, args=(cola, )) # Donde proceso1 tendra el target de la función "leerNumFichero" con los argumentos "cola"
    p2 = Process(target=sumarTodo, args=(cola,)) # Y proceso2 tendra el target de la función "sumarTodo" con los argumentos "cola"
    
    # Iniciamos la ejecución
    p1.start()
    p2.start()
    
    # Hasta que no finalice uno no va el otro
    p1.join()
    p2.join()