import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os 
import sys
import csv


class Ejercicio:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
        self.datos.dropna()
    def cotar_usuarios(self): #con esta funcion cuento cuanta gente entra en a web
        contar = self.datos["uuid"].count()
        return contar
    def transformaciones(self): #con esta funcion se cuenta cuantos clientes finalmente han realizado la conversion con un bucle
        contador = 0  
        for i in self.datos["lead_type"]:
            if i == "CALL":
                contador = contador + 1
            elif i =="FORM":
                pass
        return contador
        
hola = Ejercicio("conversiones (4).csv")
hola.cotar_usuarios()

