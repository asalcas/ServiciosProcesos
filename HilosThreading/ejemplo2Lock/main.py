from BloqueaLista import BloqueaLista

# Main que ejecute la funcion 'MiThread' 24 veces
if __name__ == "__main__":
    print("----- Soy el hilo principal -----")
    for i in range(25):
        hilo = BloqueaLista(str(i))
        hilo.start()