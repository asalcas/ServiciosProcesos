
from multiprocessing import Process, Queue


def leerFichero(cola: Queue): #Le pasamos por parámetros a la función que haremos una cola
    with open ("ejercicio3/numeros.txt", "r") as archivo: # Abrimos el archivo txt en modo lectura con el nombre de "archivo"
        for linea in archivo.readlines: # Por cada linea en el archivo
            num = int(linea) #lo guardamos en la variable num
            cola.put(num) # Enviamos a la cola "num"
            print("Enviando numero: " + str(num))
        cola.put(None) # Si no hay numeros en el archivo pasamos a la cola none para que se acabe
        
def sumarNumerosFichero(cola: Queue): #Le pasamos por parametros a la funcion que haremos una cola
    numero = cola.get() # Obtenemos el numero de la cola
    while numero is not None: # Cuendo numero (El elemento de la cola) no sea None entonces
        suma = 0
        for i in range (1, numero + 1): # Por cada numero en el elemento que se pasó por la cola
            suma += i # suma el indice a la variable suma
        print(f"Recibiendo el numero: {str(numero)}, la cuenta se hará hasta el indice {str(i)} y el resultado es: {str(suma)}")
        
if __name__ == "__main__":
    queue = Queue()
    p1 = Process(target=leerFichero, args=(queue,))
    p2 = Process(target=sumarNumerosFichero, args=(queue, ))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()