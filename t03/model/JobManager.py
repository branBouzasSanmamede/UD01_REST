from t03.utils.rutas_t03 import ruta_jobs_json, ruta_jobs_txt, sufijo_sistema
from utils.util_json import leer_json
from utils.util_menus import mostrar_encabezado
from .Job import Job
import subprocess
import time

class JobManager:
    def __init__(self):
        self.jobs = self.cargar_jobs()

    def cargar_jobs(self):
        data = leer_json(ruta_jobs_json())
        return [Job(j["run"], j["frecuencia"]) for j in data]

    def mostrar_jobs(self):
        print("\n".join(f" - {j}" for j in self.jobs))

    def ejecutar_jobs(self):
        for i, job in enumerate(self.jobs, start=1):
            mostrar_encabezado(f"Ejecutando job: job_{i:03d}")

            nombre = f"job_{i:03d}{sufijo_sistema()}"
            ruta = ruta_jobs_txt() / nombre
            ruta.parent.mkdir(parents=True, exist_ok=True)

            with open(ruta, "w", encoding="utf-8") as f:
                subprocess.run(job.run, shell=True, stdout=f, text=True)

            print(f"[OK] Guardado en: {ruta}")

            espera = job.convertir_frecuencia()
            mostrar_encabezado(f"Esperando {espera} segundos...")
            time.sleep(espera)
            print("Espera finalizada")