from multiprocessing import Process, Queue
from random import randint
from time import sleep


def producer (queue, id):  
    for i in range(10): 
        if queue.full(): #! AHORA MISMO NO SE PIERDEN PAQUETES, pero si metemos el queue.put en el else de este IF entonces si podemos hacer que pierda paquetes.
            print(f"P{id}: La cola está llena")
        queue.put(i)    
        print(f"P{id}: He puesto: {i}") 
        sleep(randint(1,5)) 
    queue.put(None) 
    print (f"El Productor P{id}, ha terminado con su arduo trabajo!")

def consumer(queue,id): 
    while True:  
        item = queue.get() 
        if queue.empty(): 
            print(f"C{id}: La cola está vacia")
        if item is None:
            break
        print(f"P{id}: He recibido: {item}") 
        sleep(randint(1,5)) 
    print (f"El Consumidor P{id}, ha terminado con su arduo trabajo!")

    #TODO AQUI EJECUTAMOS EL CÓDIGO USANDO EL MAIN: ( PARA VER EL RESULTADO BIEN, EJECUTA POR TERMINAL)
if __name__ == '__main__':
    queue = Queue(maxsize = 3)
    productores = []
    consumidores = []

    numP = randint(1,5) #! Por si queremos 

    for i in range(3):
        productores.append(Process(target = producer, args= [queue, i, ]))
        consumidores.append(Process(target = consumer, args= [queue, i, ]))

    for i in range(3):
        productores[i].start()
    for i in range(3):
        consumidores[i].start()

    for i in range(3):
        productores[i].join()
    for i in range(3):
        consumidores[i].join()

    print ("Todos los procesos han terminado")

    