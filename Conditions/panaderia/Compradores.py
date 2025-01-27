from threading import Thread

class Compradores(Thread):

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def compra_pan(self):
        pass