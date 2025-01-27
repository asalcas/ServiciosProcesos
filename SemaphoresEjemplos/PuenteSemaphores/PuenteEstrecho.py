from threading import Thread,Semaphore
import time,random

azulANSI="\033[0;34m"
amarilloANSI= "\033[1;33m"
verdeANSI="\033[0;32m"
returnWhiteANSI= "\033[0m"
rojoANSI = "\033[0;31m"

class cruzarPuente(Thread):
    

    def __init__(self):
        Thread.__init__(self)
        self.semaforoPuenteDch = Semaphore(1)
        self.semaforoPuenteIzq = Semaphore(1)

    """def cochesCruzan(self, colorCoche, direccion):
        print(f"{azulANSI} El coche: {colorCoche} 👀 entra en el puente{returnWhiteANSI}")
        self.semaforoPuenteDch.acquire()
        tiempoPelicula= random.randint(1,3)
        print(f"{rojoANSI} El coche: {colorCoche} 👀 ha cruzado el puente{returnWhiteANSI}")
        time.sleep(tiempoPelicula)
        print(f"{amarilloANSI} El usuario: {colorCoche} ha terminado de sacar dinero y se va{returnWhiteANSI}")
        self.semaforoPuente.release()
        print(f"{verdeANSI} El usuario: {colorCoche} se ha ido del banco y ha dejado su sitio para otra persona, quedan {str(self.semaforoBanco._value)}{returnWhiteANSI}")
"""
    def run(self, colorCoche, direccion):
        if self.direccion == 0:
            s