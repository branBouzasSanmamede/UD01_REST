from datetime import datetime
import os
import ctypes
import locale
import platform

def obtener_sistema():
    return platform.system().lower()

def obtener_fecha():
    return f"-{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.json"

def obtener_codificacion():
    if os.name == "nt":
        return f"cp{ctypes.windll.kernel32.GetConsoleOutputCP()}"
    else:
        return locale.getpreferredencoding(False)