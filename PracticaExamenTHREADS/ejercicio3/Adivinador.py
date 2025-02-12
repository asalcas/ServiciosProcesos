import random
from threading import Thread

class Adivino(Thread): # Creamos la clase Adivinador que hereda de Thread
    # Lo que hará que podamos trabajar con esta clase como si duera un HILO
    
    def __init__(self): # Es un constructor de la clase, y lo que hace es que cuando instanciamos un objeto Adivino
        # inicializamos el objeto con las características del objeto que queramos.
        Thread.__init__(self) # Llamamos al constructor de la clase Thread para que el objeto instanciado herede correctamente su comportamiento
        self.numero = random.randint(0,100) # A cada objeto que instanciamos le pasamos como propiedad un numero PARA que adivinen aleatorio
        self.acertante = False # Es una variable que por defecto es False, e indicará si alguien acertó o no
        
    def comprobar (self, num): # Este es una función que recibe la variable 'num' como parámetro
        respuesta = False # Inicializamos respuesta a False, para indicar si el jugador acertó o no
        if num == self.numero: # Si num 
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