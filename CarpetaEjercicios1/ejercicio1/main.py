from threading import Thread

from trabajadores import MiThread

if __name__ == "__main__":
    
    print("Ha comenzado el dia de trabajo")
    trabajadores = [MiThread()for i in range (5)]
    for trabajador in trabajadores:
        trabajador.start()