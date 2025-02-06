import random
from threading import Thread
import time 


nombres = ["Ana", "Luis", "María", "Carlos", "Elena", "Javier", "Sofía", "Pedro"]


class MiThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.nombre = random.choice(nombres)
        
    def run(self):
        print(f"Soy el trabajador {self.nombre} y empiezo ahora a trabajar.")
        time.sleep(random.randint(1,10))
        print(f"Soy el trabajador{self.nombre} y he terminado mi jornada laboral.")
        