from enum import Enum

class MultiplicadorTiempo(Enum):
    y = 365*24*3600
    M = 30*24*3600
    w = 7*24*3600
    d = 24*3600
    h = 3600
    m = 60
    s = 1