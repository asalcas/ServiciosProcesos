import random
import threading

nombres = ["Ana", "Carlos", "Laura", "Miguel", "Valentina", "Tomás", "Sofía", "Pedro", "Isabel", "Luis"]

class Contador:
    def __init__(self):
        self.valor = 0  # Contador inicializado en 0
        self.lock = threading.Lock()  # Lock para asegurar acceso atómico al contador
        self.name = random.choice(nombres)
        
    # Método para incrementar el contador de forma segura
    def incrementar(self, total):
        with self.lock:  # Asegura que solo un hilo pueda modificar el contador a la vez
            if self.obtener_valor() >= total:   # Si el contador ya alcanza el total
                return  # Sale del método 
            self.valor += 1  # Incrementar el valor del contador
    # Método para obtener el valor actual del contador
    def obtener_valor(self):
        return self.valor

    # Función que simula la operación de incrementar el contador desde múltiples hilos
def incrementar_contador(contador, total):
    while contador.obtener_valor() < total:
        contador.incrementar(total)  # Cada hilo incrementará el contador N veces
        
            
if __name__ == "__main__":
    contador = Contador()  # Crear una instancia de la clase Contador
    hilos = []  # Lista para guardar los hilos
    N = 10  # Número de hilos
    TOTAL = 1000  # Total a alcanzar

    # Crear y arrancar los hilos
    for _ in range(N):
        hilo = threading.Thread(target=incrementar_contador, args=(contador, TOTAL))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()
    # Mostrar el valor final del contador
    print(f"Valor final del contador: {contador.obtener_valor()}")


