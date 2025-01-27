from threading import Thread

class Reponedores(Thread):

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def reponer_pan(self):
        pass