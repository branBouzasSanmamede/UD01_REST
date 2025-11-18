from t05.e1.index import main as e1
from t05.e2.index import main as e2
from t05.e3.index import main as e3
from utils.util_menus import ejecutar_menu

menu = [
    (1, "Información del sistema", e1),
    (2, "Información de los servicios", e2),
    (3, "Información de los procesos", e3)
]

def main():
    ejecutar_menu(menu)

if __name__ == "__main__":
    main()