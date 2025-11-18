from t05.utils.rutas_t05 import ruta_salida_e1
from utils.util_json import guardar_json
from .SystemInfo import SystemInfo

class InfoManager:
    def __init__(self):
        self.info = SystemInfo()

    def mostrar_info(self):
        print(self.info)

    def guardar_info(self):
        guardar_json(self.info.to_json(), ruta_salida_e1())

    def recargar_info(self):
        self.info = SystemInfo()