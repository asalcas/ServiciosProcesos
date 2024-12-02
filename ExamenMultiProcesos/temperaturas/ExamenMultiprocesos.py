

from multiprocessing import Lock, Pool, Process
import os
import random


def generarTemperatura(idProceso):
    temperaturas = [round(random.uniform(1, 20),2)for _ in range(24)]
    print(temperaturas)
    
    with open(f"{idProceso}-12.txt", "w") as archivo: 
        for i in range(len(temperaturas)):
            archivo.write(f"{temperaturas[i]}\n")
            
    print("Se han generado correctamente las 31 temperaturas")

def leerFicherosMaxima(idProceso):
    with open(f"{idProceso}-12.txt", "r") as archivo:
        lineas = archivo.readlines()
    maxima_temperatura = 0
    for linea in lineas:
        
        temperatura = float(linea.strip())
        if  temperatura > maxima_temperatura:
            maxima_temperatura = temperatura
    with open(f"temperaturas/maximas.txt", "a") as archivo:
        archivo.write(f"Maximas del dia: {idProceso}-12: {maxima_temperatura}\n")
    print(f"La maxima temperatura es: {str(maxima_temperatura)}")

def leerFicherosMinima(idProceso):
    with open(f"{idProceso}-12.txt", "r") as archivominimo:
        lineas = archivominimo.readlines()
    minima_temperatura = 20
    for linea in lineas:
        
        temperatura = float(linea.strip())
        if  temperatura < minima_temperatura:
            minima_temperatura = temperatura
    with open(f"temperaturas/minimas.txt", "a") as archivo:
        archivo.write(f"Minimas del dia: {idProceso}-12: {minima_temperatura}\n")
    print(f"La minima temperatura es: {str(minima_temperatura)}")
    

if __name__ == "__main__":

    diasDiciembre = [(i,) for i in range(1, 32)]  # Cada día del 1 al 31 como una tupla
    diasDiciembreNum = len(diasDiciembre) 
    lock = Lock()
    with Pool(processes = 31) as poolGenerartemperaturas:
        resultados = poolGenerartemperaturas.starmap(generarTemperatura,diasDiciembre)

    with Pool(processes = 31) as poolLasMaximasTemp:
        resultados = poolLasMaximasTemp.starmap(leerFicherosMaxima,diasDiciembre)

    with Pool(processes= 31) as poolLasMinimasTemp:
        resultados = poolLasMinimasTemp.starmap(leerFicherosMinima,diasDiciembre)
    