import threading
from Cine import SalaCine
import random
from threading import Thread, Semaphore

nombres = [
    "Juan", "María", "Pedro", "Lucía", "Carlos",
    "Sofía", "Miguel", "Marta", "Andrés", "Laura",
    "Javier", "Ana", "Fernando", "Clara", "David",
    "Elena", "Alberto", "Patricia", "Diego", "Paula"
]



if __name__ == "__main__":

    # variable lanzamiento de los hilos
    irAlCine = SalaCine()
    asistenciaSala = [threading.Thread(target = irAlCine.entrada ,args=(random.choice(nombres),)) for _ in range(100)]
    for irAlCine in asistenciaSala:
        irAlCine.start()