
from multiprocessing import Process, Pool
from time import sleep


def sumaNumeros(id, num):
    suma = 0
    for i in range(1, num + 1):
        suma += i
        print(f"El proceso {str(id)}: Ha realizado la suma de los numeros hasta {str(i)} y el resultado es {str(suma)}")
        sleep(1)
    return suma
if __name__ == '__main__':
    with Pool(processes = 3) as pool: #? En esta linea le decimos CUANTOS procesos a la vez queremos que haga
        numeros = [(1, 6),(2, 3),(3, 5),(4, 1),(5, 8),(6, 2)] #? En esta otra, el numero de procesos que hay para hacer
        # Por lo que al ejecutar el programa, irá de 3 en 3, 
        # osea hara dos vueltas ya que son 6 los que le mandamos.
        resultados = pool.starmap(sumaNumeros, numeros) 
        #? pool.starmap() hace que le digamos al pool que función realizar con que datos a tener en cuenta
        # En este caso los datos son las tuplas de ID y Num 
        # que le pasaremos a la función, y despues lo guardaremos en resultados
        print(f"Resultados: {resultados}")
        