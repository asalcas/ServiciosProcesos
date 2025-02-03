import threading
from EjemploProfesor import *

if __name__ == "__main__":
    plato = Event() # Creo un evento
    plato.set() # Seteo el evento a False
    ratones = [Raton(f"Raton {i}", plato) for i in range(5)] # Ratones
    for raton in ratones: #Iniciamos proceso
        raton.start()
    for raton in ratones: #Cerramos proceso
        raton.join()