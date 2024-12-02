#coding: latin1



from multiprocessing import Process
from time import sleep


def sumarNum(id, num):
    suma = 0 
    for i in range (1 , num+1):
        suma += i
        print ("Proceso " + str(id) + ": Suma de todos los valores hasta el "+ str(i) + ": "+ str(suma))
        sleep(1)

if __name__ == '__main__':
    p1 = Process(target= sumarNum, args = (1, 2)) #id y num (Pasados por parametro)
    p2 = Process(target= sumarNum, args = (2, 4))
    p3 = Process(target= sumarNum, args = (3, 5)) 

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()