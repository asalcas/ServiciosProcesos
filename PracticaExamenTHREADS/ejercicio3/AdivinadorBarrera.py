import random
from threading import Thread, Lock

class Adivino(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.numero = random.randint(0,100)
        self.acertante = False
        
    def comprobar (self,num):
        respuesta = False
        if num == self.numero:
            print("Has acertado")
            self.acertante = True
            respuesta = True
        return respuesta
    
class Jugador(Thread):
    def __init__(self,adivino,nombre):
        Thread.__init__(self, name= nombre)
        self.adivino = adivino
        self.nombre = nombre
        
    def run(self):
        while not self.adivino.acertante:
            miNum = random.randint(0,100)
            res = self.adivino.comprobar(miNum)
            if(res):
                print(f"{self.nombre} ha acertado! ✅")
            else:
                print(f"{self.nombre} sigue jugando ❌")
                
if __name__ == "__main__":
    adivino = Adivino()
    adivino.start()
    jugadores = [Jugador(adivino, f"Jugador{i}") for i in range(10)]
    for jugador in jugadores:
        jugador.start()
    for jugador in jugadores:
        jugador.join()