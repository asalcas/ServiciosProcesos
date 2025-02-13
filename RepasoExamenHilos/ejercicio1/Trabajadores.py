from threading import Thread
import random
import time

# Para poder diferenciar bien los hilos, vamos a ponerle un nombre a cada uno, para separarlos en vez de usar numeros.
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

class Trabajadores(Thread): # Creamos la clase Trabajadores heredando de Thread
    
    def __init__(self): # Init es el constructor, donde le decimos que:
        Thread.__init__(self) # Ejecutará en forma de Hilo
        self.name = random.choice(nombres) # Le damos un nombre aleatorio al Hilo
        self.colorElegido = random.choice(colors_and_styles) # Le damos un color aleatorio al Hilo
        self.horas = 0 # E inicializamos una variable creada a 0
    
    def run(self): # Una vez se ejecute la clase, con .start() o .join()
        while True: # El ejercicio pedia un bucle infinito...
            self.horas += 1 # Por cada ejecución queremos que sume una hora al contador
            print(f"{self.colorElegido} Soy {self.name} y estoy trabajando! LLevo {self.horas} hora trabajando" + "\033[0m")
            time.sleep(random.randint(1,10))
            print(f"{self.colorElegido} Soy {self.name} y he terminado de trabajar y he trabajado {self.horas} horas" + "\033[0m")
        
if __name__ == "__main__": # Creamos el main
    trabajadores_hilos = [] # CREAMOS UNA LISTA donde posteriormente...
    
    for _ in range(5): # meteremos todas las instancias de Trabajadores()
        trabajador = Trabajadores()
        trabajadores_hilos.append(trabajador) # Relleno la lista de Trabajadores()... : Trabajador1: Carlos, color: Rojo 
        #                                                                               Trabajador2:  Laura, color: Verde

    for trabajador in trabajadores_hilos:  # Por cada TRABAJADOR (Carlos, Laura...)  
        trabajador.start()    # Comienza la acción del run()
            
    for trabajador in trabajadores_hilos:  # Por cada TRABAJADOR (Carlos, Laura...)  
        trabajador.join()     # Finaliza la acción
            