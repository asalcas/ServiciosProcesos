from threading import Thread, Lock
from ejercicio1Panaderia.ClasePanaderia import compra_pan

class Comprador(Thread):

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        poderComprar = compra_pan()
