
#En este caso, vuelve a realizar la comunicación entre procesos pero usando tuberías (Pipe), 
# de forma que la función que se encarga de leer los números del fichero se los envíe (send) 
# al proceso que se encarga de la suma. El proceso que suma los números tiene que recibir (recv) 
# un número y realizar la suma. Una vez que el proceso que lee el fichero termine de leer números 
# en el fichero, debe enviar un None. El que recibe números dejará de realizar sumas cuando reciba 
# un None.

from multiprocessing import Pipe, Process


def leerFichero(t1Left): # Le pasamos a la función la ruta de la tubería que tendrá (t1Left, que es la parte izquierda, encargada de enviar información) 
    with open("ejercicio4/numerosEjercicio4.txt", "r") as Archivo: # Le pasamos la ruta del archivo y le decimos que tendrá permisos de lectura
        for linea in Archivo.readlines(): # Leemos linea a linea el txt
            num = int(linea) # Guardamos lo que contenga la linea en la variable num
            t1Left.send(num) # Enviamos lo que se ha guardado
            print(f"Enviando numero {str(num)}") # Hacemos el print de que enviamos
        t1Left.send(None) # Si no teniamos más líneas, le pasamos None para acabar con la ejecución

def sumarNumerosFichero(t1Right): # Le pasamos a la función la ruta de la tubería que tendrá (t1Right, que es la parte derecha, encargada de recibir datos)
    num = t1Right.recv() # Recibimos los datos de la otra parte de la Tuberia
    suma = 0 
    while num is not None: # Cuando haya información a tratar
        suma += num # Lo incrementamos a suma 
        print(f"La suma de los numeros es: {suma}") # Lo imprimimos
        num = t1Right.recv()   # Y le pasamos otro valor nuevo

if __name__ == "__main__":
    t1Left, t1Right = Pipe() # Declaramos cual serán los nombres de ambas salidas del Pipe() "Tubería"
    
    p1 = Process(target=leerFichero, args=(t1Left, )) # Le asignamos un target al proceso y en el argumento, el nombre de la posicion del Pipe()
    p2 = Process(target=sumarNumerosFichero, args= (t1Right, )) # Le asignamos un target al proceso y en el argumento, el nombre de la posicion del Pipe()
    
    # Iniciamos los procesos
    p1.start()
    p2.start()
    
    # Hasta que no acabe un proceso, no empieza el otro.
    p1.join()
    p2.join()