import os
import time

def convertirMinusculas(archivo):
    inicio = time.time()
    # Abrir archivo
    with open(archivo, 'r') as file:
        data = file.read()
    # Convertir a minusculas
    data = data.lower()
    # Crear un nuevo nombre de archivo
    nuevo_archivo = archivo.replace('.html', '_minusculas.html')
    # Guardar archivo
    with open(nuevo_archivo, 'w') as file:
        file.write(data)
    fin = time.time()
    tiempo = fin - inicio
    return tiempo

def convertirMinusculasCarpeta(carpeta):
    tiempo_total = 0
    # Lista de archivos en la carpeta
    archivos = os.listdir(carpeta)
    # Recorrer archivos
    for archivo in archivos:
        # Si es un archivo html
        if archivo.endswith('.html'):
            # Convertir a minusculas
            tiempo = convertirMinusculas(carpeta + '/' + archivo)
            tiempo_total += tiempo
            with open('tiempos.txt', 'a') as file:
                file.write(f'Archivo: {archivo}, Tiempo: {tiempo} segundos\n')
    with open('tiempos.txt', 'a') as file:
        file.write(f'Tiempo total: {tiempo_total} segundos\n')

def main():
    # Carpeta
    carpeta = 'C:\/Users/oem/Videos/Fase 2 Proyectos de ingenieria de Software/Actividad 4/HtmlSinEtiquetas'
    # Convertir a minusculas
    convertirMinusculasCarpeta(carpeta)

# Ejecutar la función principal
if __name__ == "__main__":
    main()