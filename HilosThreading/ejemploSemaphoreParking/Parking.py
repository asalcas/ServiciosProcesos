from threading import Thread, Lock, Semaphore
import time

import random

class Parking(Thread):

    semaforoParking = Semaphore(5)

    def __init__(self, nombre):
            Thread.__init__(self, name = nombre)


    def run(self):
            # Simulamos el acceso a las cajas del super
            print(f"{amarilloANSI}El coche, 🚗 {self.name} va a un aparcamiento {returnWhiteANSI}")
            Parking.semaforoParking.acquire()
            tiempoAparcado = random.randint(1,10)
            print(f"{verdeANSI}El coche, 🚗 {self.name} ha aparcado durante {tiempoAparcado} minutos {returnWhiteANSI}")
            # Cada cliente es atendido un tiempo distinto
            time.sleep(tiempoAparcado)
            print(f"{azulANSI}El conductor 🚗 {self.name} se esta montando en el coche {returnWhiteANSI}")
            Parking.semaforoParking.release()
            print(f"El coche, 🚗 {self.name} se va del Parking y queda {rojoANSI} {str(Parking.semaforoParking._value)} {returnWhiteANSI}")
            

azulANSI="\033[0;34m"
amarilloANSI= "\033[1;33m"
verdeANSI="\033[0;32m"
returnWhiteANSI= "\033[0m"
rojoANSI = "\033[0;31m"
