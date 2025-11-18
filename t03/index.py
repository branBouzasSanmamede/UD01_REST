from utils.util_menus import ejecutar_menu
from .model.JobManager import JobManager

job_manager = JobManager()

menu = [
    (1, "Listar json", job_manager.mostrar_jobs),
    (2, "Ejecutar comandos", job_manager.ejecutar_jobs)
]

def main():
    ejecutar_menu(menu)