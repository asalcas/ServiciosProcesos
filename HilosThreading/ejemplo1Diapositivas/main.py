from claseThreading import MiThread

# Main que ejecute la funcion 'MiThread' 24 veces
if __name__ == "__main__":
    print("----- Soy el hilo principal -----")

    for i in range(25):
        hilo = MiThread (str(i))
        hilo.start()