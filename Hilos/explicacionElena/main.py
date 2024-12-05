


from ejemplo import Ejemplo


if __name__ == "__main__":
    lista = []
    print("Soy el hilo principal")

    for i in range(0,10):
        hilo = Ejemplo(i)
        hilo.start()
        lista.append(hilo)

    for h in lista: 
        h.join()