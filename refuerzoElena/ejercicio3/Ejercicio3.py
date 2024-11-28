


from multiprocessing import Process, Queue


def leerFichero(cola: Queue):
    with open ("ejercicio3/numeros.txt", "r") as archivo:
        for linea in archivo.readlines():
            num = int(linea)
            cola.put(num)
            print ("Añadiendo: "+ str(num))
        cola.put(None)

def sumaNum(cola: Queue):
    numero = cola.get()
    while numero is not None:
        suma = 0
        for i in range (1,numero +1): 
            suma += i
        suma += numero
        print("Suma hasta " + str(numero) + ": " + str(suma))
        numero = cola.get()
    return suma


if __name__ == '__main__':
    queue = Queue()
    p1 = Process(target = leerFichero, args=(queue,))
    p2 = Process(target = sumaNum, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()