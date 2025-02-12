# Coding: latin-1
"""
Contador compartido
Crea un programa que utilice 10 hilos para incrementar un contador compartido. Deben dejar de contar cuando el contador llegue a 1000. Para ello, en el método run() se seguirá incrementando la variable mientras ésta sea menor que 1000.
Observa cómo la concurrencia puede afectar el resultado final.
"""


import random
from threading import Thread





class MiThread(Thread):
    contador = 0
    def __init__(self):
        Thread.__init__(self)
        self.suma = 0
        self.lock()
        self.meta=1000
        
    def run(self):
        with self.lock():
            self.suma += 1
            if self.suma <= self.meta:
                print(self.suma)
                return
            
            