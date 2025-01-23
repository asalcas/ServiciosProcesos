from Banco import *
import threading
import random


nombres = [
    "Juan", "María", "Pedro", "Lucía", "Carlos",
    "Sofía", "Miguel", "Marta", "Andrés", "Laura",
    "Javier", "Ana", "Fernando", "Clara", "David",
    "Elena", "Alberto", "Patricia", "Diego", "Paula"
]


if __name__ == "__main__":
    irAlBanco = BancoSemaforo()
    genteBanco = [threading.Thread(target = irAlBanco.sacar_dinero, args=(random.choice(nombres),)) for _ in range(10)]
    for irAlBanco in genteBanco:
        irAlBanco.start()