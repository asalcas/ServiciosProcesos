"""
Imagina que estás gestionando un supermercado y tienes varias cajas registradoras funcionando al mismo tiempo. Cada caja atiende a un cliente a la vez,
y los clientes tienen que esperar si todas las cajas están ocupadas. Tu objetivo es simular este sistema para entender cómo gestionar los recursos y cómo mejorar la eficiencia del supermercado.
- Debes simular N cajas registradoras (hilos) que atienden a los clientes.
- Cada cliente tiene un tiempo de atención diferente (simulado con time.sleep).
- Los clientes llegan a la fila de manera secuencial, pero deben ser atendidos en paralelo si hay cajas disponibles (una única cola para todas las cajas).
Al final, debes mostrar:
- Cuánto tiempo total tardaron en ser atendidos todos los clientes.
- Cuántos clientes atendió cada caja.
"""
import threading    
import time

#coding: latin1
class Mercadono:
    



    def agregar_cliente(nombre):
        cola_supermercado.append()



    def atender_cliente(nombre, ncola, tiempo):
        print(f"Cliente {nombre} ha entrado en la caja: {ncola}")
        time.sleep(tiempo) # Simula tiempo de descarga
        print (f"El cliente ha sido atendido con exito en el numero de la cola {ncola}")


    if __name__ == "__main__":

        hilos = [
        threading.Thread(target=atender_cliente, args=("Juan", 3)),
        threading.Thread(target=atender_cliente, args=("Chia", 5)),
        threading.Thread(target=atender_cliente, args=("Manuel", 2)),
        ]
        for hilo in hilos:
            hilo.start()
        for hilo in hilos:
            hilo.join()
        print("Todos las cajas han finalizado con los clientes")
        # EJEMPLO PARA TRATAR CON COLAS:
        """
        # Representamos la cola con una lista
        cola_supermercado = []
        # Función para agregar un cliente a la cola
        def agregar_cliente(nombre):
            cola_supermercado.append(nombre)
            print(f"Cliente {nombre} agregado a la cola.")
        # Función para atender a un cliente (FIFO)
        def atender_cliente():
            if cola_supermercado:
                cliente_atendido = cola_supermercado.pop(0)
                print(f"Atendiendo al cliente: {cliente_atendido}")
            else:
                print("No hay clientes en la cola para atender.")
        # Ejemplo de uso
        agregar_cliente("Juan")
        agregar_cliente("Ana")
        agregar_cliente("Luis")
        atender_cliente()  # Atendemos a Juan
        atender_cliente()  # Atendemos a Ana
        atender_cliente()  # Atendemos a Luis
        atender_cliente()  # Intento de atender cuando la cola está vacía"""