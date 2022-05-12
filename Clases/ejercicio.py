import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Ejercicio:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
    def cotar_usuarios(self):
        self.datos["uuid"].count()
        
hola = Ejercicio("navegacion (4).csv")
hola.cotar_usuarios()