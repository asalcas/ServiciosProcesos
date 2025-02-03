from threading import Thread, Event, Lock
import time
import random

class Empresa:
    def __init__(self):
        self.evento_ventas = Event()
        
        # Da la señal de que las ventas pueden realizarse
    def comenzar_Ventas(self):
        print("Empresa: ¡La venta ha comenzado! 🎉")
        self.evento_ventas.set()
        time.sleep(5)
        
        # Da la señal de que las ventas se han acabado
    def cerrar_Ventas(self):
        print("\nEmpresa: ⏰ Venta cerrada. No hay más tickets.")
        self.evento_ventas.clear()              