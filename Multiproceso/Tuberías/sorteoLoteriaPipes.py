from multiprocessing import Process, Pipe
from random import randint

def loteria(pipe):
    print ("Bienvenidos a la loteria COMEEENZAMOS")
    lista = []
    while True: 
        if pipe.recv() == 0:
            numLoteria = randint(1,100)
            while numLoteria in lista:
                numLoteria = randint(1,100)
            lista.append(numLoteria)
            pipe.send(numLoteria)
        else:
            pipe.close()
            break

def ludopata(pipe):
    creditosQueTengo = 10
    while True:
        while creditosQueTengo>0:
            pipe.send(0) # Quiero un numero
            numeroBombo = pipe.recv()
            apuesta = randint(1,100)
            print("El numero que ha salido es:", numeroBombo)
            print(f"Vaya yo tengo el: {apuesta}" )
            if (numeroBombo == apuesta):
                print("VAMOOOO HE GANAOOOO!! :D")
                pipe.send(1) #Se acaba el juego
                break
            else: 
                print("Me cago en la mar serena")
                creditosQueTengo -=1
                print (f"No pasa na me quedan {creditosQueTengo}, seguro que lo doblo!")
    pipe.close()

if __name__ == '__main__':
    pipe1, pipe2 = Pipe()
    p1 = Process(target=loteria, args=(pipe1, ))
    p2 = Process(target=ludopata, args=(pipe2, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()