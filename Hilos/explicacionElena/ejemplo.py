
from threading import Thread
from time import sleep


class Ejemplo(Thread): 
    def __init__(self, num): 
        Thread.__init__(self) # Esto es el SUPER(), para heredar en java
        self.num = num

    #El metodo que va a ejecutarse
    def run(self): 
        sleep(1)
        print("Soy el hilo", self.num)
        print("Mi nombre es", self.name) # Name es un atributo de la clase Thread