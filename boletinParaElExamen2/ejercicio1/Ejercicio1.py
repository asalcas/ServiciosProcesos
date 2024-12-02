
from multiprocessing import Pool

#ESTE ES DURO, cosas a tener en cuenta!
def leerArchivo(): 
    with open("ejercicio1/ficheroVocales.txt", "r") as archivo: #Abrimos el archivo en modo lectura
        textoALeer = archivo.readlines() # PASAMOS TODO el archivo en el return
    return textoALeer

def cuentaVocales(vocales, textoALeer): # Le pasamos por parametros texto a leer (el archivo anterior) y vocales [("a"),("e"),("i"),("o"),("u")]
    contador = 0
    for linea in textoALeer: # Por cada linea en el archivo (2)
        contador += linea.lower().count(vocales) # Cuenta el numero de una VOCAL en cuestión
    print(f"En el fichero la vocal {vocales} aparece {contador} veces.")
    
if __name__ == "__main__":
    leerTexto = leerArchivo() # Lee el archivo
    vocales = ["a", "e", "i", "o", "u"] # Vocales guardadas
    with Pool(processes= 5) as pool:
        resultados = pool.starmap(cuentaVocales, [("a", leerTexto), ("e", leerTexto),("i", leerTexto), ("o", leerTexto), ("u", leerTexto)])
        # Esto de abajo es lo mismo para simplificar los dos parametros que tendra "cuentaVocales"
        #resultados = pool.starmap(cuentaVocales, [(vocal, leerTexto)for vocal in vocales])