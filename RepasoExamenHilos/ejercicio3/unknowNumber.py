import random
from threading import Thread, Lock
import time

nombres = ["Ana", "Carlos", "Laura", "Miguel", "Valentina", "Tomás", "Sofía", "Pedro", "Isabel", "Luis"]

# Al igual que la lista anterior de nombres, aquí creamos una lista de comandos de color para hacer mas sencillo todo.
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
    "\033[1;37m"
]

class numeroOculto(Thread):
    numeroOculto = 27
    def __init__(self):
        Thread.__init__(self)
        self.name = random.choice(nombres) # Esto tambien
        self.color = random.choice(colors_and_styles)
        self.numeroAdivinar = random.randint(1,100) # Esto tengo que ponerlo en el run
        self.lock = Lock()
        
    def run(self):
        funcionando = True
        with self.lock:
            
            while funcionando:
                print(f"El hilo {self.name} ha generado un valor aleatorio: {self.numeroAdivinar}")
                if self.numeroAdivinar == numeroOculto:
                    print(f"{self.name} ha encontrado el numero! Es: {numeroOculto}")
                    funcionando = False
                else:
                    print(f"El hilo {self.name} va a volver a intentarlo tras esperar un poco...")
                    time.sleep(random.randint(1,5))
                
if __name__ == "__main__":
    jugador = numeroOculto()
    preparacion=[]
    
    for _ in range(10):
        preparacion.append(jugador)
        
    for jugador in preparacion:
        jugador.start()
        
    for jugador in preparacion:
        jugador.join()
    
    
