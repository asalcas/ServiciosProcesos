
from random import randint
from threading import Thread
from time import sleep


class Trabajador(Thread):
    def __init__(self,nombre):
        Thread.__init__(self, name = nombre)


    def run(self):
        print(f"Soy {self.name} y estoy trabajando")
        sleep(randint(1,10))
        print(f"Soy {self.name} y he terminado de trabajar")