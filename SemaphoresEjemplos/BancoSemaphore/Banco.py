from threading import Thread, Semaphore
import random
import time

azulANSI="\033[0;34m"
amarilloANSI= "\033[1;33m"
verdeANSI="\033[0;32m"
returnWhiteANSI= "\033[0m"
rojoANSI = "\033[0;31m"


class BancoSemaforo(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.semaforoBanco = Semaphore(3)

    def sacar_dinero(self, nombreUsuario):
        print(f"{azulANSI} El usuario: {nombreUsuario} 👀 va al banco{returnWhiteANSI}")
        self.semaforoBanco.acquire()
        tiempoPelicula= random.randint(1,3)
        print(f"{rojoANSI} El usuario: {nombreUsuario} 👀 ha sacado dinero{returnWhiteANSI}")
        time.sleep(tiempoPelicula)
        print(f"{amarilloANSI} El usuario: {nombreUsuario} ha terminado de sacar dinero y se va{returnWhiteANSI}")
        self.semaforoBanco.release()
        print(f"{verdeANSI} El usuario: {nombreUsuario} se ha ido del banco y ha dejado su sitio para otra persona, quedan {str(self.semaforoBanco._value)}{returnWhiteANSI}")