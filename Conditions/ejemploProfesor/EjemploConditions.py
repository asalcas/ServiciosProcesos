from threading import Thread, Condition
import time
import random


class Ejemplo(Thread):
    lista = [False, False, False, False, False]
    cond = Condition()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)


    def run(self):
        # Se genera una posición aleatoria de la lista
        num = random.randint(0,4)
        # Mientras el objeto esté siendo usado por otro hilo no lo puede usar el actual
        Ejemplo.cond.acquire()
        while Ejemplo.lista[num] == True:
            print(f"El hilo {self.name}, está esperando a que se libere la posición, {num}")
            Ejemplo.cond.wait()

        # Una vez que veo que esta libre lo reservo para mí
        Ejemplo.lista[num]= True
        #Aqui podemos liberar el bloque por que ya hemos modificado la lista
        Ejemplo.cond.release()

        print(f"El hilo {self.name}, está usando el objeto {num}")
        time.sleep(random.randint(1,10))
        print(f"El hilo {self.name}, ha terminado de usar el objeto, {num}")

        # Antes de modificar la lista volvemos a bloquear
        Ejemplo.cond.acquire()
        Ejemplo.lista[num] = False
        Ejemplo.cond.notify_all()
        # Una vez hemos notificado liberamos el bloqueo
        Ejemplo.cond.release()


if __name__ == "__main__":
    
    lista=[]
    for i in range (10):
        lista.append(Ejemplo(i,))


    for ejemplo in lista:
        ejemplo.start()
        ejemplo.join()