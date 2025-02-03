from threading import Thread
import time
from Empresa import Empresa

class Comprador(Thread):
    def __init__(self, nombre):
        self.nombre = nombre
        
    def run(self):
        print(f"{self.nombre} quiere comprar. 🧍")
        while not Empresa.evento_ventas.is_set():
            Empresa.evento_ventas.wait()    

        while Empresa.evento_ventas.is_set(): 
            print(f"{self.nombre} está comprando... 💳")
            
        else:
            print(f"{self.nombre} no pudo comprar. ❌")
            
            #🎫