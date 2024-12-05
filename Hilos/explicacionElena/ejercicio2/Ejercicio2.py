from threading import Lock, Thread

class Contador(Thread):
    contador = 0 # Atributo estatico
    bloqueo = Lock() # OBJETO LOCK A NIVEL DE CLASE

    def __init__(self, nombre): # Constructor
        Thread.__init__(self, name = nombre)

    def run(self):

        Contador.bloqueo.acquire() # CREA UN BLOQUEO DE LO QUE ESTÉ ENTRE ACQUIRE Y RELEASE
        print("Soy el hilo", self.name)
        while Contador.contador < 1000: 
            Contador.contador += 1
        Contador.bloqueo.release() #PARA SOLTAR EL BLOQUEO
        print(f"Valor del {Contador.contador}")