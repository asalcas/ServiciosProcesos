from Comprador import Comprador
from Comprador import Empresa
from threading import Event


if __name__ == "__main__":
    
    Empresa.comenzar_Ventas
    clientes = [Comprador(f"Cliente {i}", clientes) for i in range(5)] # Ratones
    for comprador in clientes: #Iniciamos proceso
        comprador.start()
    for comprador in clientes: #Cerramos proceso
        comprador.join()