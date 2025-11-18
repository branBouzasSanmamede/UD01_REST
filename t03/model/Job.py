from t03.enums.MultiplicadorTiempo import MultiplicadorTiempo

class Job:
    def __init__(self, run: str, frecuencia: str):
        self.run = run
        self.frecuencia = frecuencia

    def __str__(self):
        return f"Comando: {self.run}, Frecuencia: {self.frecuencia}"
    
    def convertir_frecuencia(self):
        total_segundos = 0
        for parte in self.frecuencia.split(":"):
            if parte:
                valor, unidad = int(parte[:-1]), parte[-1]
                total_segundos += valor * MultiplicadorTiempo[unidad].value 
        return total_segundos