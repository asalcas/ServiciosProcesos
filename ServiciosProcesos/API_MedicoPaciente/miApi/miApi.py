#coding: latin1

from ctypes import cast
from re import I
from pip._vendor import requests
num = -1
while num != 0: 
    num = int(input("Introduce un N� de usuario para solicitar datos: "))
    if(num>0 ):
            response = requests.get(api_url + str(num))
            api_url = "https://jsonplaceholder.typicode.com/todos/" + str(num)
            response = requests.get(api_url)
            print(response.json())
            
    elif(num <0 ):
        print("Opci�n incorrecta. Vuelve a intentarlo")
    else :
        salir = True
    print("salida")
    

