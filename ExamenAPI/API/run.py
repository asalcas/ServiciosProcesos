import json
from flask import *


app = Flask(__name__)

def leerFicherosVehiculos():
    archivo = open("C:\\Users\\alvaro.salvador\\Desktop\\ExamenAPI\\API\\BD\\vehicles.json", "r")
    Vehiculos = json.load(archivo)
    archivo.close()
    return Vehiculos

def escribirFicherosVehiculos(Vehiculos):
    archivo = open("C:\\Users\\alvaro.salvador\\Desktop\\ExamenAPI\\API\\BD\\vehicles.json", "w")
    json.dump(Vehiculos, archivo)
    archivo.close()

@app.route('/')
def index():
    return 'Esta es la pagina de inicio!'

@app.get("/vehicles")
def get_vehiculo():
    Vehiculos = leerFicherosVehiculos()
    return Vehiculos

@app.get("/vehicles/<int:id>")
def get_vehiculo_id(id):  # Le pasamos por parametros ese INT que recibe en la ruta
    Vehiculos = leerFicherosVehiculos()
    for vehiculo in Vehiculos:  # Creamos una variable dentro de Vehiculos que según el ID que le den será uno u otro
        if vehiculo["id"] == id:
            return vehiculo, 200  # EL ID concuerda, consulta exitosa
    return {"Error": "Paciente not found"}, 404  # Error en la consulta, ID NO EXISTE

def _add_siguienteID_vehiculo():  # METODOS PARA ENCONTRAR EL MÁXIMO ID DE LOS Vehiculos y sumarle un ID más
    Vehiculos = leerFicherosVehiculos()
    return max(vehiculo["id"] for vehiculo in Vehiculos) + 1 if not Vehiculos else 1

@app.post('/vehicles')
def add_vehicles():
    Vehiculos = leerFicherosVehiculos()
    if request.is_json:
        Vehiculo = request.get_json()
        Vehiculo['id'] = _add_siguienteID_vehiculo()
        Vehiculos.append(Vehiculo)
        #if (Vehiculo["matricula", "marca", "modelo"] == True):
        escribirFicherosVehiculos(Vehiculos)
        return jsonify(Vehiculo), 201
    return {"Error": "Request must be JSON"}

@app.patch("/vehicles/<int:id>")
def modificar_estadoVehiculo(id):
    Vehiculos = leerFicherosVehiculos()
    if request.is_json:
        actualizarVehiculo = request.get_json()
        for Vehiculo in Vehiculos:
            if Vehiculo ["id"] == id:
                for element in Vehiculo:
                    Vehiculo[element] = actualizarVehiculo[element]

                escribirFicherosVehiculos(Vehiculos)
                return jsonify(Vehiculo), 200
            
@app.delete("/vehicles/<int:id>")
def delete_vehicle(id):

    Vehiculos = leerFicherosVehiculos()
    for Vehiculo in Vehiculos:
        if Vehiculo["id"] == id:
            Vehiculos.remove(Vehiculo)
            escribirFicherosVehiculos(Vehiculos)
            return Vehiculo, 200
    return {"Error": "Paciente not found"}


if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 5050)