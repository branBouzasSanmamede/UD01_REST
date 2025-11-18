from utils.util_menus import ejecutar_menu
from t06.measure_comand.measure_comand import measure_comand

menu = [ (1, "Measure Comand", measure_comand) ]

def main():
    ejecutar_menu(menu)

if __name__ == "__main__":
    main()