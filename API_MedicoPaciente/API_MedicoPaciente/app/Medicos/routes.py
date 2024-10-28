import json
from flask import *
from flask import Blueprint, jsonify

from API_MedicoPaciente.app.Pacientes.routes import leerFicherosPacientes


def leerFicherosMedicos():
    archivo = open("DB/medicos.json", "r")
    Medicos = json.load(archivo)
    archivo.close()
    return Medicos

def escribirFicherosMedicos(Medicos):
    archivo = open("DB/medicos.json", "w")
    json.dump(Medicos, archivo)
    archivo.close()

medicosBP = Blueprint('Medicos', __name__)



@medicosBP.get("/")  # DETERMINAMOS la ruta para hacer la petición
def get_medicos():
    Medicos = leerFicherosMedicos()
    return jsonify(Medicos)



@medicosBP.get("/<int:id>")  # DETERMINAMOS la ruta para hacer la petición diciendo: El INT que te den será la conexión entre el ID y el registro
def get_medico_id(id):  # Le pasamos por parametros ese INT que recibe en la ruta
    Medicos = leerFicherosMedicos()
    for Medico in Medicos:  # Creamos una variable dentro de Pacientes que según el ID que le den será uno u otro
        if Medico["Id"] == id:
            return Medico, 200  # EL ID concuerda, consulta exitosa
    return {"Error": "Medicos not found"}, 404  # Error en la consulta, ID NO EXISTE

@medicosBP.get("/<int:id>/pacientes")
def get_pacientes(id):
    Pacientes = leerFicherosPacientes()
    pacientes_Medico = []
    for Paciente in Pacientes:
        if Paciente["IdMedico"] == id:
            pacientes_Medico.append(Paciente)
    if len(pacientes_Medico) > 0:
        return pacientes_Medico, 200
    else:
        return {"Error": "No se encontraron pacientes"}, 404

def _add_siguienteID_medicos (): # METODOS PARA ENCONTRAR EL MÁXIMO ID DE LOS MEDICOS y sumarle un ID más
    Medicos = leerFicherosMedicos()
    if not Medicos: # Si no hay registros, retorna 1 Para tener el ID: 1
        return 1
    return max(Medico["Id"] for Medico in Medicos) + 1

@medicosBP.post("/")
def add_medico():
    Medicos = leerFicherosMedicos()
    if request.is_json:
        Medico = request.get_json()

        Medico["Id"] = _add_siguienteID_medicos()
        Medicos.append(Medico)

        escribirFicherosMedicos(Medicos)
        return Medico, 201
    return {"Error": "Request must be JSON"}

@medicosBP.put("/<int:id>")
@medicosBP.patch("/<int:id>")
def update_medico(id):
    Medicos = leerFicherosMedicos()
    if request.is_json:
        newMedico = request.get_json()

        for Medico in Medicos:
            if Medico["Id"] == id:
                for element in newMedico:
                    Medico[element] = newMedico[element]
                    escribirFicherosMedicos(Medicos)
                return Medico, 200
    return {"Error": "Medicos not found"}

@medicosBP.delete("/<int:id>")
def delete_medico(id):
    Medicos = leerFicherosMedicos()
    for Medico in Medicos:
        if Medico["Id"] == id:
            Medicos.remove(Medico)
            escribirFicherosMedicos(Medicos)
            return Medico, 200
    return {"Error": "Medicos not found"}
