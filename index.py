from utils.util_menus import ejecutar_menu
from t03.index import main as t03
from t05.index import main as t05
from t06.index import main as t06

menu = [
    (1, "UD01_T03 --> json_cron", t03),
    (2, "UD01_T05 --> psutil", t05),
    (3, "UD01_T06 --> measure-comand", t06)
]

def main():
    ejecutar_menu(menu)

if __name__ == "__main__":
    main()