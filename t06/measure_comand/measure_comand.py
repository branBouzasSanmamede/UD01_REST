from utils.util_menus import mostrar_encabezado
from utils.util_simples import obtener_codificacion
import re
import time
import subprocess

def measure_comand():

    mostrar_encabezado("Measure Command")

    match = re.search(r"\{(.*)\}", input("Introduce el comando entre llaves { }: "))
    
    if not match:
        print("Error: Debes introducir un comando entre llaves { ... }")
        return
    
    command = match.group(1).strip()
    mostrar_encabezado(f"Ejecutando comando: {command}")

    start = time.time()
    try:
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding=obtener_codificacion())

        for l in iter(proc.stdout.readline, ''): print(l, end='')

        proc.wait()
        end = time.time()

        mostrar_encabezado("Tiempo")
        print(f"Tiempo de ejecución: {end - start:.2f} segundos")

    except Exception as e:
        print(f"Error ejecutando el comando: {e}")