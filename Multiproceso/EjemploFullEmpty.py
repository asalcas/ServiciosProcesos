from multiprocessing import Process, Queue
from random import randint
from time import sleep


def producer (queue):  
    for i in range(10): 
        if queue.full(): #! COMPROBAMOS SI ESTÁ LLENA LA COLA
            print("La cola está llena")
        queue.put(i)    
        print(i, 'Enviado') 
        sleep(randint(1,5)) #! CREAMOS EL DESTIEMPO PARA PODER VER CUANDO ESTÁ LA COLA LLENA/VACIA
    queue.put(None) 
    print ("El Productor ha terminado con su arduo trabajo!")

def consumer(queue): 
    while True:  
        item = queue.get() 
        if queue.empty(): #! COMPROBAMOS SI ESTÁ VACIA LA COLA
            print("La cola está vacia")
        if item is None:
            break
        print(item, 'Recibido') 
        sleep(randint(1,5)) #! CREAMOS EL DESTIEMPO PARA PODER VER CUANDO ESTÁ LA COLA LLENA/VACIA
    print ("El Consumidor ha terminado con su arduo trabajo!")

    #TODO AQUI EJECUTAMOS EL CÓDIGO USANDO EL MAIN: ( PARA VER EL RESULTADO BIEN, EJECUTA POR TERMINAL)
if __name__ == '__main__':
    queue = Queue(maxsize = 3)

    proceso1 = Process(target = producer, args= [queue,])
    proceso2 = Process(target = consumer, args= [queue,])

    proceso1.start()
    proceso2.start()

    proceso1.join()
    print('Proceso 1 terminado')

    proceso2.join()
    print('Terminado')