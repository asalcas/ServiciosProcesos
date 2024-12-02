
from multiprocessing import Pipe, Process


def leerNumFichero(t1Left):
    with open ("ejercicio8/numerosEjercicio8.txt", "r") as archivo:
        for linea in archivo.readlines():
            idProceso, num1, num2 = map(int, linea.strip().split())
            print(f"Para el proceso {idProceso}: Enviamos los numeros {num1} y {num2}")
            t1Left.send((idProceso, num1, num2)) #! FALLO QUE ME ESTABA DANDO, RECUERDA QUE ESTAS PASANDO UNA TUPLA ESPABILAO
        t1Left.send(None)


def sumarTodo(t1Right):
    numeros = t1Right.recv()
    while numeros is not None:
        suma = 0
        idProceso, num1, num2 = numeros
        if num1 > num2:
            num1, num2 = num2, num1
        suma = sum(range(num1, num2 + 1)) #! CUIDADO NO METER LA SUMA DENTRO DEL IF, LA CUENTA ES FUERA
        print(f"En el proceso {idProceso}: La suma total de {num1} y {num2} es: {suma}")
        numeros =t1Right.recv()


if __name__ == "__main__":
    t1Left, t1Right = Pipe()
    p1 = Process(target=leerNumFichero, args=(t1Left, ))
    p2 = Process(target=sumarTodo, args=(t1Right, ))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()