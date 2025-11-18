from utils.util_rutas import PROYECTO_RAIZ
from utils.util_simples import obtener_sistema

JOBS_BASE_JSON_PATH = PROYECTO_RAIZ / 't03' / 'json'
JOBS_BASE_TXT_PATH  = PROYECTO_RAIZ / 't03' / 'txt'

def ruta_jobs_json():
    carpeta = "windows" if obtener_sistema() == "windows" else "linux"
    return JOBS_BASE_JSON_PATH / carpeta / "jobs.json"

def ruta_jobs_txt():
    carpeta = "windows" if obtener_sistema() == "windows" else "linux"
    return JOBS_BASE_TXT_PATH / carpeta

def sufijo_sistema():
    return "_w.txt" if obtener_sistema() == "windows" else "_l.txt"