from threading import Thread,Condition
import random


cond = Condition()

class Panaderia(Thread):
    panes_tiene = 10

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        
    def gestionar_tienda(self):
        with Panaderia.cond:
            while Panaderia.panes_tiene > 0:
                print(f"El cliente, {self.name} está esperando para comprar el pan")
                Panaderia.cond.wait()

            Panaderia.