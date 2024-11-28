from multiprocessing import Process, Pool, Value, Lock

def incrementos(id, variable, lock):
    for i in range(10000):
        with lock:
            variable.value += 1 
            print(f"El proceso {id} incrementa el valor")
        #! ESTA PARTE ES PROBLEMATICA POR QUE
        #! PUEDEN SOBREESCRIBIRSE LA VARIABLE POR LOS PROCESOS, POR LO QUE
        #! NECESITA QUE LE PONGAMOS LOCK() PARA PROTEGER LA SECCION CRÍTICA
    return variable


if __name__ == '__main__':
    #? SOLUCIÓN DE DAVID, NO ENTIENDO MUCHO
    contador = Value("i", 0)
    procesos = []
    lock = Lock()
    procesos = [Process (target = incrementos, args= (contador,lock,)) for _ in range(4)]

    for p in procesos:
        p.start()
    for p in procesos:
        p.join()

    print(f"El valor final del contador es: {contador.value}")



    #numerodeProcesos = 4
    #variable = Value("i", 0)
    #procesos = []
    #for i in range(numerodeProcesos):
    #    p = Process(target=incrementos , args=(variable, ))
    #    p.start()
    #    procesos.append(p)
    
    #for p in procesos:
    #    p.join()
    #
    #print("Resultado ", variable.value)
