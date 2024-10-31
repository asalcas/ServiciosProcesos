
import token
from flask import Flask
import requests
import app 

#DENTRO DE LAS FUNCIONES QUE NECESITEN VERIFICACIÓN
try:
   respuesta = requests.post("http://localhost:5050/lista",
   headers={"Authorization": "Bearer " + token})
except Exception as e:
   print(e)

# Si la petición es exitosa
if respuesta.status_code == 200:
   # Muestra el json correspondiente a la petición
   print(respuesta.json())
# Si no, muestra este mensaje
else:
   print("Se ha producido un error")
print("Pulsa una tecla para poder continuar...")	# Pausa la ejecución durante 2 segundos


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)

