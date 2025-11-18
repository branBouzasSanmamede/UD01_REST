from pathlib import Path
import json

def leer_json(ruta_completa):
    ruta = Path(ruta_completa)
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error leyendo el archivo JSON: {e}")
        return None

def guardar_json(objeto, ruta_completa):
    ruta = Path(ruta_completa)
    try:
        with open(ruta, "w") as f:
            json.dump(objeto, f, indent=2)
        print(f"Informacion guardada correctamente en: {ruta}")
    except Exception as e:
        print(f"Error guardando el archivo JSON: {e}")