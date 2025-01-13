from Ejercicio1 import Trabajador

if __name__ == "__main__":
    hilo1 = Trabajador("Pepe")
    hilo2 = Trabajador("Juanito Golondrina")
    hilo3 = Trabajador("Justiniano")
    hilo4 = Trabajador("Batman")
    hilo5 = Trabajador("Chari")
    
    hilo1.start()
    hilo2.start()
    hilo3.start()
    hilo4.start()
    hilo5.start()