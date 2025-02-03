from threading import Thread, Event
import random
import time


class Raton(Thread):
    def __init__(self,nombre,event: Event):
        Thread.__init__(self,name = nombre)
        self.evento = event
        
    def run(self):
        while not self.evento.is_set():
            self.evento.wait()
        self.evento.clear()
        print(f"El ratón, {self.name}, toma el control del plato")
        time.sleep(random.randint(1,3))
        print(f"El ratón {self.name}, termina de comer")
        self.evento.set()