from carpetaInterfaz import auth
from carpetaInterfaz import funciones

def opcionMedicos():
    funcionando = True
    while (funcionando == True):
        print("============================================")
        print("==                                        ==")
        print("==     Selecciona que quieres hacer       ==")
        print("==                                        ==")
        print("============================================")
        
        print("1. Get MÉDICOS")
        print("2. Post MÉDICOS")
        print("3. Patch/put MÉDICOS")
        print("4. Delete MÉDICOS")
        print("5. Salir")
        opcion = input("¿Que quieres hacer? Seleccione un numero: ")

        if opcion == 1:
            funciones.getMedico()
        
        elif opcion == 2:
            funciones.postMedico()
            pass
        elif opcion == 3:
            funciones.patchMedico()
            pass
        elif opcion == 4:
            funciones.deleteMedico()
            pass
        elif opcion == 5:
            print ("Muchas gracias, hasta pronto!!")         
            funcionando = False
        else:
            print("Ha ocurrido un error inesperado, has introducido un numero valido?")

def opcionPacientes():
    funcionando = True
    while (funcionando == True):
        print("============================================")
        print("==                                        ==")
        print("==     Selecciona que quieres hacer       ==")
        print("==                                        ==")
        print("============================================")
        
        print("1. Get PACIENTES")
        print("2. Post PACIENTES")
        print("3. Patch/put PACIENTES")
        print("4. Delete PACIENTES")
        print("5. Salir")
        opcion = input("¿Que quieres hacer? Seleccione un numero: ")

        if opcion == 1:
            funciones.getPaciente()
        
        elif opcion == 2:
            funciones.postPaciente()
            pass
        elif opcion == 3:
            funciones.patchPaciente()
            pass
        elif opcion == 4:
            funciones.deletePaciente()
            pass
        elif opcion == 5:
            print ("Muchas gracias, hasta pronto!!")         
            funcionando = False
        else:
            print("Ha ocurrido un error inesperado, has introducido un numero valido?")
            
            
def registrarUsuario():
    auth.registro()