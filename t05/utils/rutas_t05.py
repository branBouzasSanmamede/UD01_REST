from utils.util_simples import obtener_fecha
from utils.util_simples import obtener_sistema
from utils.util_rutas import PROYECTO_RAIZ

BASE = PROYECTO_RAIZ / "t05" / "e1" / "json"

def ruta_salida_e1():
    sub = "systemInfo_w" if obtener_sistema() == "windows" else "systemInfo_l"
    return BASE / sub / f"{obtener_fecha()}.json"