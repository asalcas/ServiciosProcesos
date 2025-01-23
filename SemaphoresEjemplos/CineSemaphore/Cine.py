from threading import Thread, Semaphore
import time
import random


azulANSI="\033[0;34m"
amarilloANSI= "\033[1;33m"
verdeANSI="\033[0;32m"
returnWhiteANSI= "\033[0m"
rojoANSI = "\033[0;31m"

class SalaCine(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.semaforoCine = Semaphore(20)


    def entrada(self,nombreUsuario):
        print(f"{azulANSI} El espectador: {nombreUsuario} 👀 va al cine{returnWhiteANSI}")
        self.semaforoCine.acquire()
        tiempoPelicula= random.randint(1,3)
        print(f"{rojoANSI} El espectador: {nombreUsuario} 👀 ha visto la pelicula durante {tiempoPelicula} horas{returnWhiteANSI}")
        time.sleep(tiempoPelicula)
        print(f"{amarilloANSI} El espectador: {nombreUsuario} ha terminado de ver la pelicula y se levanta del cine{returnWhiteANSI}")
        self.semaforoCine.release()
        print(f"{verdeANSI} El espectador: {nombreUsuario} se ha ido del cine y ha dejado su sitio para otra persona, quedan {str(self.semaforoCine._value)}{returnWhiteANSI}")