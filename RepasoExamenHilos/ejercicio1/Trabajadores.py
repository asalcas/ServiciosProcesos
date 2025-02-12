from threading import Thread
import random
import time

nombres = ["Ana", "Carlos", "Laura", "Miguel", "Valentina", "Tomás", "Sofía", "Pedro", "Isabel", "Luis"]

colors_and_styles = [
    "\033[0;31m",
    "\033[0;32m",
    "\033[0;33m",
    "\033[0;34m",
    "\033[0;35m",
    "\033[0;36m",
    "\033[0;37m",
    "\033[1;31m",
    "\033[1;32m",
    "\033[1;33m",
    "\033[1;34m",
    "\033[1;35m",
    "\033[1;36m",
    "\033[1;37m",
    "\033[1m",
    "\033[2m",
    "\033[3m",
    "\033[4m",
    "\033[5m",
    "\033[7m",
    "\033[9m",
    "\033[0m"
]

class Trabajadores(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.name = random.choice(nombres)
        self.colorElegido = random.choice(colors_and_styles)
        self.horas = 0
    
    def run(self):
        while True:
            self.horas += 1
            print(f"{self.colorElegido} Soy {self.name} y estoy trabajando! LLevo {self.horas} hora trabajando" + "\033[0m")
            time.sleep(random.randint(1,10))
            print(f"{self.colorElegido} Soy {self.name} y he terminado de trabajar y he trabajado {self.horas} horas" + "\033[0m")
        
if __name__ == "__main__":
    trabajadores_hilos = []
    
    for _ in range(5):
        trabajador = Trabajadores()
        trabajador.start()
        trabajadores_hilos.append(trabajador) #estoy como rellenando una lista de hilos
        
    for trabajador in trabajadores_hilos:
        trabajador.join()
            