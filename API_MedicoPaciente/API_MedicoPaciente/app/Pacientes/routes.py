import json
from flask import *
from flask import Blueprint, jsonify


def leerFicherosPacientes():
    archivo = open("DB/pacientes.json", "r")
    Pacientes = json.load(archivo)
    archivo.close()
    return Pacientes



def escribirFicherosPacientes(Pacientes):
    archivo = open("DB/pacientes.json", "w")
    json.dump(Pacientes, archivo)
    archivo.close()


pacientesBP = Blueprint('pacientes', __name__)


@pacientesBP.get("/")  # DETERMINAMOS la ruta para hacer la petición
def get_pacientes():
    Pacientes = leerFicherosPacientes()
    return jsonify(Pacientes)


@pacientesBP.get("/<int:id>")  # DETERMINAMOS la ruta para hacer la petición diciendo: El INT que te den será la conexión entre el ID y el registro
def get_paciente_id(id):  # Le pasamos por parametros ese INT que recibe en la ruta
    Pacientes = leerFicherosPacientes()
    for Paciente in Pacientes:  # Creamos una variable dentro de Pacientes que según el ID que le den será uno u otro
        if Paciente["Id"] == id:
            return Paciente, 200  # EL ID concuerda, consulta exitosa
    return {"Error": "Paciente not found"}, 404  # Error en la consulta, ID NO EXISTE


def _add_siguienteID_pacientes():  # METODOS PARA ENCONTRAR EL MÁXIMO ID DE LOS PACIENTES y sumarle un ID más
    Pacientes = leerFicherosPacientes()
    if not Pacientes:
        return 1
    return max(Paciente["Id"] for Paciente in Pacientes) + 1


@pacientesBP.post("/")
def add_paciente():
    Pacientes = leerFicherosPacientes()
    if request.is_json:
        Paciente = request.get_json()

        Paciente["Id"] = _add_siguienteID_pacientes()
        Pacientes.append(Paciente)
        escribirFicherosPacientes(Pacientes)
        return Paciente, 201
    return {"Error": "Request must be JSON"}


@pacientesBP.put("/<int:id>")
@pacientesBP.patch("/<int:id>")
def update_paciente(id):
    Pacientes = leerFicherosPacientes()
    if request.is_json:
        newPaciente = request.get_json()

        for Paciente in Pacientes:
            if Paciente["Id"] == id:
                for element in newPaciente:
                    Paciente[element] = newPaciente[element]
                    escribirFicherosPacientes(Pacientes)
                return Paciente, 200
    return {"Error": "Paciente not found"}


@pacientesBP.delete("/<int:id>")
def delete_pacientes(id):
    Pacientes = leerFicherosPacientes()
    for Paciente in Pacientes:
        if Paciente["Id"] == id:
            Pacientes.remove(Paciente)
            escribirFicherosPacientes(Pacientes)
            return Paciente, 200
    return {"Error": "Paciente not found"}
