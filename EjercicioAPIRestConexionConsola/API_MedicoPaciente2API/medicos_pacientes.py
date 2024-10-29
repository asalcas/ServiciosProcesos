from flask import Flask

app= Flask(__name__) #__name__ ES UNA VARIABLE ESPECIAL de Python que se refiere automaticamente al nombre del módulo en el que se encuentra el código.

Medicos = [
        {
            "Id": 1,
            "Nombre": "Jorge",
            "Apellidos": "Fernandez Vicioso",
            "Nº Colegiado": "123456",
            "Especialidad": "Neurología",
        },
        {
            "Id": 2,
            "Nombre": "Lucía",
            "Apellidos": "Martinez Sánchez",
            "Nº Colegiado": "654321",
            "Especialidad": "Cardiología",
        }
]
Pacientes = [
        {
            "Id": 1,
            "DNI": "12345678A",
            "Nombre": "Jesús",
            "Apellidos": "Gutierrez Rodriguez",
            "SegSocial": "1111111111",
            "FNacimiento": "27/07/1974",
            "IdMedico": 1,
        },
        {
            "Id": 2,
            "DNI": "12345678B",
            "Nombre": "Fátima",
            "Apellidos": "Ruiz Mejías",
            "SegSocial": "2222222222",
            "FNacimiento": "12/09/1986",
            "IdMedico": 1,
        },
        {
            "Id": 3,
            "DNI": "12345678C",
            "Nombre": "Javier",
            "Apellidos": "Fernandez Cid",
            "SegSocial": "333333333",
            "FNacimiento": "22/03/2000",
            "IdMedico": 2,
        },
]

with open("DB/medicos.json", "w") as file:
    json.dump(Medicos, file, indent=4)

with open("DB/pacientes.json", "w") as file:
    json.dump(Pacientes, file, indent=4)


medicosBP = Blueprint('Medicos', __name__)
pacientesBP = Blueprint('Pacientes', __name__)


def leerFicherosPacientes():
    archivo = open("DB/pacientes.json", "r")
    Pacientes = json.load(archivo)
    archivo.close()
    return Pacientes


def escribirFicherosPacientes(Pacientes):
    archivo = open("DB/pacientes.json", "w")
    json.dump(Pacientes, archivo)
    archivo.close()







# SIN MODIFICAR PARA LEER Y ESCRIBIR ARCHIVOS
# @app.post("/medicos")
# def add_medico():
#
#
#     if request.is_json:
#         Medicos = request.get_json()
#
#         Medicos["Id"] = _add_siguienteID_medicos()
#         Medicos.append(Medicos)
#
#
#         return Medicos, 201
#     return {"Error": "Request must be JSON"}


















@app.route("/") # Definimos la ruta raiz
def index(): # Decimos que se muestra cuando accedamos al index
    return 'Hola a todos! :D'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)