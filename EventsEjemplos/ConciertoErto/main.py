from Comprador import Comprador
from Comprador import Empresa
from threading import Event


if __name__ == "__main__":
    
    oferta = Empresa.evento_ventas # Creo un evento
    oferta.set() # Seteo el evento a False
    clientes = [Comprador(f"Cliente {i}", clientes) for i in range(5)] # Ratones
    for comprador in clientes: #Iniciamos proceso
        comprador.start()
    for comprador in clientes: #Cerramos proceso
        comprador.join()