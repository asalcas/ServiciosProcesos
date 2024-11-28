
from multiprocessing import Pipe, Process
from random import *


def generarIp(t1Left):
    for i in range (1,11):
        num1 = randint(1,255)
        num2 = randint(1,255)
        num3 = randint(1,255)
        num4 = randint(1,255)
        ip = f"{num1}.{num2}.{num3}.{num4}"
        t1Left.send(ip)
    #t1Left.send(None)

def clasificarIp(t1Right, t2Left):
    for _ in range(1,11):
        ip = t1Right.recv()
        octetos = ip.split(".")
        primeros = int(octetos[0])
        if primeros > 0 and primeros <= 233:
            t2Left.send(ip)
    t2Left.send(None)

def pintaIp(t2Right):
    ip = t2Right.recv()
    while ip is not None:
        octetos = ip.split(".")
        primero = int(octetos[0])
        if primero <= 127:
            print(ip, "Clase A")
        elif primero <= 191:
            print(ip, "Clase B")
        else:
            print(ip, "Clase C")
        ip = t2Right.recv() #! Para poder hacer otra iteracción


if __name__ == '__main__':
    t1Left, t1Right = Pipe()
    t2Left, t2Right = Pipe()
    proceso1 = Process(target= generarIp, args = (t1Left,))
    proceso2 = Process(target= clasificarIp, args = (t1Right,t2Left))
    proceso3 = Process(target = pintaIp, args = (t2Right, ))

    proceso1.start()
    proceso2.start()
    proceso3.start()

    proceso1.join()
    proceso2.join()
    proceso3.join()