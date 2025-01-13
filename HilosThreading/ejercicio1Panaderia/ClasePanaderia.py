from threading import Thread, Lock

class Panaderia(Thread):
    barrasPan = 7
    bloqueo = Lock()

    def __init__(self, cantidadPan):
        Thread.__init__(self)
        self.cantidadPan = cantidadPan

    def compra_pan(self):
        poderComprar = False

        if(Panaderia.barrasPan > 0):
            Panaderia.barrasPan -1
            poderComprar = True
        
        return poderComprar

    def run(self, poderComprar):
        if (poderComprar):
            