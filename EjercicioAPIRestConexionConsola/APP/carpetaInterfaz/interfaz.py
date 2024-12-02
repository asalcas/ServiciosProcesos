#coding: latin1 

#from API.app.Users import routes #ERROR AQUI-- 
from carpetaInterfaz import opciones
from flask import Flask
import requests
from carpetaInterfaz import auth


def interfazUsuario():
    
    print("============================================")
    print("==              Bienvenido                ==")
    print("============================================")
    print("                                            ")
    print("1.Iniciar Sesion")
    print("2.Crear una cuenta")
    
    opcion = int(input("Seleccione una opcion: "))
    if (opcion==1):
        token = auth.login()
    elif(opcion==2):
        auth.registro()
        token = auth.registro()
    if not token:
        print("No se pudo autenticar. Salida del programa.")
        return
    
    funcionando = True
    while (funcionando == True):
        print("============================================")
        print("==                                        ==")
        print("==     Selecciona que quieres hacer       ==")
        print("==                                        ==")
        print("============================================")
        
        print("1. Opciones con: MÉDICOS")
        print("2. Opciones con: PACIENTES")
        print("3. Salir")
        opcion = input("¿Que quieres hacer? Seleccione un numero: ")

        if opcion == 1:
            opciones.opcionMedicos()
        
        elif opcion == 2:
            opciones.opcionPacientes()
            
        elif opcion == 3:
            print ("Muchas gracias, hasta pronto!!")         
            funcionando = False
        else:
            print("Ha ocurrido un error inesperado, has introducido un numero valido?")
            
