from threading import Thread

class CuentaVocales(Thread):
    def __init__(self,nombre):
        Thread.__init__(self)
        self.numVocales = 0
        self.nombreVocales = nombre