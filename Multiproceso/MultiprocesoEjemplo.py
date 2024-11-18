
from multiprocessing import Process, Queue
from time import sleep


def producer (queue):  #* Es el encargado de Introducir Procesos a la COLA DE PROCESOS
   for i in range(5): # Hacemos un bucle que iterará desde 0 a 4 = (0, 1, 2, 3, 4)
      queue.put(i)    # Le estamos introduciendo a la cola el valor de i en cada iteración 
      print(i, 'Enviado') # Imprimimos el indice más el mensaje
      sleep(2) # Hacemos que tenga una pausa de dos segundos entre iteración
   queue.put(None) # Cuando acabemos, le decimos que pase un None para finalizar
   print ("El Productor ha terminado con su arduo trabajo!")

def consumer(queue): #* Es el encargado de Recoger Procesos de la COLA DE PROCESOS
   while True: # Hacemos que entre en un bucle infinito 
      item = queue.get() # Haciendo que vaya recogiendo todos los PROCESOS (Items)
      if item is None: # Le decimos que si encuentra que item es None que salga del bucle infinito
            break
      print(item, 'Recibido') # Imprimimos el proceso (El item por donde vamos) recibido con su mensaje correspondiente
      sleep(1) # Le damos una pausa de un segundo entre cada lectura
   print ("El Consumidor ha terminado con su arduo trabajo!")

   #TODO AQUI EJECUTAMOS EL CÓDIGO USANDO EL MAIN: ( PARA VER EL RESULTADO BIEN, EJECUTA POR TERMINAL)
if __name__ == '__main__':
   queue = Queue()

   proceso1 = Process(target = producer, args= [queue,])
   proceso2 = Process(target = consumer, args= [queue,])

   proceso1.start()
   proceso2.start()

   proceso1.join()
   print('Proceso 1 terminado')

   proceso2.join()
   print('Terminado')
