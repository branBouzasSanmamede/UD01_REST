import shutil

def mostrar_encabezado(texto, sep="#"):
    ancho = shutil.get_terminal_size().columns
    texto = f' {texto} '

    relleno_total = ancho - len(texto)
    izq = relleno_total // 2
    der = relleno_total - izq

    print(f"\n{sep * izq + texto + sep * der}\n")

def mostrar_menu(opciones):
    lineas = []
    max_len = 0 
    opt_salir = f"Opcion 0: Salir"
    for num, desc, _ in opciones:
        linea = f"Opcion {num}: {desc}"
        lineas.append(linea)
        if len(linea) > max_len:
            max_len = len(linea)
    
    if len(opt_salir) > max_len:
        max_len = len(opt_salir)

    separador = "-" * max_len
    mostrar_encabezado("Menú de opciones")
    print(separador)
    print(opt_salir)
    for l in lineas:
        print(l)
    print(separador)

    return int(input("Opcion: "))

def ejecutar_menu(opciones):
    opt = mostrar_menu(opciones)
    while opt != 0:
        for num, _, func in opciones:
            if opt == num:
                func()
                break
        else:
            print("Opcion invalida! ")
        
        opt = mostrar_menu(opciones)
    print("Hasta luego!")