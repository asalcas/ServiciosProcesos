from multiprocessing import Pool, Process
from time import sleep


def sumarNum(id, num):
    suma = 0 
    for i in range (1 , num+1):
        suma += i
        print ("Proceso " + str(id) + ": Suma de todos los valores hasta el "+ str(i) + ": "+ str(suma))
        sleep(1)
        
    return suma    

if __name__ == '__main__':
    with Pool(processes = 3) as pool:
        numeros = [(1,2),(2,4),(3,5),(4,7),(5,9)]   # Si queremos identificar el proceso, en vez de mandar solo
                                                    # El numero a donde queremos llegar, también le mandaremos el id
                                                    # en forma de TUPLA
        resultados = pool.starmap(sumarNum, numeros)

        print("Resultados: ", resultados)