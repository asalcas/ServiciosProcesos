
from multiprocessing import Process
from time import sleep


def sumarNumeros(id, numero):
    suma = 0
    for i in range( 1, numero +1):
        suma += i
        print(f"El proceso: {str(id)} Ha realizado la suma hasta {str(i)}, dando lugar al resultado: {str(suma)}")
        sleep(1)
        
if __name__ == "__main__":
    p1 = Process(target=sumarNumeros, args=(1,4))
    p2 = Process(target=sumarNumeros, args=(2,8))
    p3 = Process(target=sumarNumeros, args=(3,3))
    
    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()