from threading import Thread, Condition
import time
import random
from panaderia.PanaderiaJuanito import *
from panaderia.Compradores import *
from panaderia.Reponedores import *


if __name__ == "__main__":
    NUM_COMPRADORES = 50 # Primero determinamos que cantidad de clientes tendremos en la "Panadería"
    panificadoraSevilla = Panaderia() # Abrimos una nueva panaderia con el nombre "panificadoraSevilla"
    lista = [] # Aquí es donde guardaremos la lista de personajes que van a interactuar en nuestra panadería: "Compradores" y
    # "Reponedores"
    
    for i in range(NUM_COMPRADORES):
        lista.append(Compradores(i,panificadoraSevilla, ))

    lista.append(Reponedores(panificadoraSevilla, )) # Contratamos un reponedor de panes en la tienda

    for c in lista:
        c.start()

    for c in lista: 
        c.join()