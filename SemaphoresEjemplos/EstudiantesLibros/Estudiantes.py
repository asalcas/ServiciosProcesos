# Coding: latin-1

import random
from threading import Condition, Thread
import time


class Biblioteca(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)
        self.libros = [False,False,False,False,False,False,False,False,False,False]
    


class Estudiante(Thread):
    cond = Condition();
    librosACoger = random.randint(0,4)
    
    def __init__(self,nombre):
        Thread.__init__(self, name = nombre)
        self.nombre=nombre

    def run(self):
        libro1 = random.randint(0,10)
        libro2 = random.randint(0,10)
        self.cogerLibro(libro1, libro2)
        
    def cogerLibro(self, libro1,libro2):
        
        with self.cond:
            while (Biblioteca.libros[libro1] == False and Biblioteca.libros[libro2] == False) and libro1 != libro2:
                print(f"El estudiante, {self.name} está esperando que los libros que quieren esten libres.")
                self.cond.wait()
                
            Biblioteca.libros[self.librosACoger] = True
            
            print(f"El estudiante {self.name} ha cogido los libros: {libro1} y {libro2}")
            tiempo_leyendo = random.randint(3,5)
            print(f"El estudiante {self.name} los lee y los devuelve en {tiempo_leyendo} minutos")
            time.sleep(tiempo_leyendo)
            print(f"El estudiante {self.name} termina los libros, y va a devolver los libros.")
            
            with self.cond:
                Biblioteca.libros[Estudiante.librosACoger] = False
                self.cond.notifyAll()
                
                    
                
if __name__ == "__main__":
    estudiante = Estudiante()
    for i in range (10):
        estudiante(i)
