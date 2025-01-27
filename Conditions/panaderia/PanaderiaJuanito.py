from threading import Thread,Condition
import random


cond = Condition()

class Panaderia(Thread):
    panes_tiene = 10

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        
    