import threading
from PuenteEstrecho import *
from threading import Thread,Semaphore

colores = [
    "Azul", "Blanco", "Negro", "Rojo", "Amarillo",
    "Gris", "Verde", "Naranja"
]

if __name__ == "__main__":
    cocheCruzaPuente = cruzarPuente()
    cochePuente = [threading.Thread(target = cocheCruzaPuente.cochesCruzan, args=(random.choice(colores),)) for _ in range(10)]
    for cocheCruzaPuente in cochePuente:
        cocheCruzaPuente.start()

"""if __name__ == "__main__":
    for i in range(5):
        coche = PasoPuente(f"Coche{i+1}", random.randint(0,1))
        coche.start()
        coche.join()"""