from threading import Thread,Semaphore
import time,random


azulANSI="\033[0;34m"
amarilloANSI= "\033[1;33m"
verdeANSI="\033[0;32m"
returnWhiteANSI= "\033[0m"
rojoANSI = "\033[0;31m"

def cocheCruzando(colorCoche):
            print(azulANSI + f"El coche {colorCoche} de la derecha entra en el puente" + returnWhiteANSI)
            tiempoCruzando = random.randint(1,5);
            print(f"El coche {colorCoche} se pega {tiempoCruzando} minutos para cruzar")
            time.sleep(tiempoCruzando)
            print(f"El coche{colorCoche} sale del puente")
            
            
class cruzarPuente(Thread):
    

    def __init__(self):
        Thread.__init__(self)
        self.semaforoPuenteDch = Semaphore(1)
        self.semaforoPuenteIzq = Semaphore(1)

    
    def run(self, colorCoche, direccion):
        if self.direccion == 0:
            self.semaforoPuenteDch.acquire()
            self.semaforoPuenteIzq.acquire()
            cocheCruzando(colorCoche)
            self.semaforoPuenteDch.release()
            self.semaforoPuenteIzq.release()
            
        if self.direccion == 1:
            self.semaforoPuenteDch.acquire()
            self.semaforoPuenteIzq.acquire()
            cocheCruzando(colorCoche)
            self.semaforoPuenteDch.release()
            self.semaforoPuenteIzq.release()
    