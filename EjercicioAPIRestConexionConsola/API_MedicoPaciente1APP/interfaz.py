#coding: latin1

from app.login import login


def interfazUsuario():
    funcionando = True
    while (funcionando == True):
        print("============================================")
        print("==                                        ==")
        print("==     Selecciona que quieres hacer       ==")
        print("==                                        ==")
        print("============================================")
        
        print("1. GET MÉDICOS")
        print("2. ")
        print("3. ")
        print("4. ")
        print("5. Salir")
        opcion = input("¿Que quieres hacer? Seleccione un numero: ")

        if opcion == 1:
            getMedico()
        
        elif opcion == 2:
            #codigo a hacer
        elif opcion == 3:
            #codigo a hacer
        elif opcion == 4:
            #codigo a hacer
        elif opcion == 5:
            print ("Muchas gracias, hasta pronto!!")         
            funcionando = False
        else:
            print("Ha ocurrido un error inesperado, has introducido un numero valido?")