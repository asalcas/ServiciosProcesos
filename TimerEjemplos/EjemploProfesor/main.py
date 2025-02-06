
from threading import Timer
import time


def funcion():
    print("SayHello!")
    
if __name__ == "__main__":
    temporizador = Timer(5, funcion)
    temporizador.start()
    max = 5
    print("Esperando a que se ejecute la funcion: ")
    for indice in range (5):
        time.sleep(1)
        print(f"Quedan {max - indice} segundos")
    temporizador.join()
    