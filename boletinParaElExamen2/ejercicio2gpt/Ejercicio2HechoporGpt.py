from multiprocessing import Pool
import random
import os

def generaNumeros(rutaAEscribir):
    """
    Genera 6 números aleatorios entre 1 y 10 con dos decimales
    y los guarda en el archivo especificado por rutaAEscribir.
    """
    notasAlumnos = [round(random.uniform(1, 10), 2) for _ in range(6)]
    print(f"Notas generadas: {notasAlumnos}")
    with open(rutaAEscribir, "w") as archivo:
        for nota in notasAlumnos:
            archivo.write(f"{nota}\n")


def calcularMedia(rutaFicheroNotas, nombreAlumno):
    """
    Lee las notas de un fichero, calcula su media y la guarda
    en el archivo medias.txt junto con el nombre del alumno.
    """
    with open(rutaFicheroNotas, "r") as archivo:
        notas = [float(linea.strip()) for linea in archivo]
        media = round(sum(notas) / len(notas), 2)
        
    medias_path = "ejercicio2gpt/medias.txt"
    os.makedirs(os.path.dirname(medias_path), exist_ok=True)
    with open(medias_path, "a") as archivo_medias:
        archivo_medias.write(f"La media de {nombreAlumno} es: {media}\n")
    print(f"Media de {nombreAlumno} calculada es: {media}")


def leerMedias():
    """
    Lee el archivo medias.txt, identifica la máxima media,
    e imprime el alumno con la nota más alta.
    """
    medias_path = "ejercicio2gpt/medias.txt"
    if not os.path.exists(medias_path):
        print("El archivo medias.txt no existe.")
        return

    with open(medias_path, "r") as archivo:
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
    # Rutas y nombres de alumnos
    nombres_alumnos = ["Carlos", "Ana", "Pedro", "Maria", "Juan", "Lucia", "Raul", "Sara", "Paula", "Antonio"]
    base_path = "ejercicio2gpt"
    os.makedirs(base_path, exist_ok=True)

    # Generar archivos de notas
    rutasNotas = [os.path.join(base_path, f"Alumno{i+1}.txt") for i in range(len(nombres_alumnos))]
    
    # Generar notas en paralelo
    with Pool(processes=10) as poolGenerarNotas:
        poolGenerarNotas.map(generaNumeros, rutasNotas)

    # Calcular medias de los alumnos en paralelo
    argumentosCalcularMedia = [(ruta, nombre) for ruta, nombre in zip(rutasNotas, nombres_alumnos)]
    with Pool(processes=10) as poolCalcularMedia:
        poolCalcularMedia.starmap(calcularMedia, argumentosCalcularMedia)

    # Leer las medias y encontrar la máxima
    leerMedias()