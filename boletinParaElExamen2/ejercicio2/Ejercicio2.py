

from multiprocessing import Pool
import random

def generaNumeros(rutaAEscribir):
    notasAlumnos = [round(random.uniform(1, 10), 2) for _ in range(6)] #! AQUI HAY QUE EXPLICAR
    print(notasAlumnos)
    with open (rutaAEscribir, "w") as archivo:
        for nota in notasAlumnos:
            archivo.write(f"{nota}\n")


def calcularMedia(ficheroALeer, nombreAlumno):
    with open (ficheroALeer, "r") as archivo:
        notas = [float(linea.strip()) for linea in archivo]
        media = round(sum(notas) / len(notas),2)
        
        with open ("ejercicio2/medias.txt", "a") as archivo_medias:
            archivo_medias.write(f"La media de {nombreAlumno} es: {media}\n")
        print(f"Media de {nombreAlumno} es: {media}")
    
def leerMedias():
    with open("ejercicio2/medias.txt", "r") as archivo:
        lineas = archivo.readlines()
        maxima_media = 0
        alumno_maxima = ""
        for linea in lineas:
            if " es: " not in linea:
                continue
            alumno, media = linea.split(" es: ")
            media = float(media.strip())
            
            if media > maxima_media:
                maxima_media = media
                alumno_maxima = alumno.strip()
                
        print(f"Máxima media: {maxima_media}, Alumno: {alumno_maxima}")
    
if __name__ == "__main__":
    generaNumeros("ejercicio2/rutaNotaAlumno.txt")
    calcularMedia("ejercicio2/rutaNotaAlumno.txt", "Juan")
    leerMedias()
    nombres_alumnos = ["Carlos", "Ana", "Pedro", "Maria", "Juan", "Lucia", "Raul", "Sara", "Paula", "Antonio"]
    rutaEscribir = "medias.txt"
    rutaLeer= "rutaNotaAlumno.txt"
    
    with Pool(processes = 10) as poolGenerarNotas:
        resultadosGenerarNotas = poolGenerarNotas.map(generaNumeros, rutaEscribir)
    with Pool(processes=10) as poolCalcularMedia:
        resultadosCalcularMedia = poolCalcularMedia.starmap(calcularMedia,(rutaEscribir, nombres_alumnos))
    
    