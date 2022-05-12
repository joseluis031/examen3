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
        contador_call = 0  
        contador_form = 0
        for i in self.datos["lead_type"]:
            if i == "CALL":
                contador_call = contador_call + 1
            elif i =="FORM":
                contador_form = contador_form + 1
        return contador_call, contador_form
    def recurrentes(self):
        contador_recurrente = 0
        contador_no_recur = 0
        for i in self.datos["user_recurrent"]:
            if i == "True":
                contador_recurrente = contador_recurrente + 1
            elif i == "False":
                contador_no_recur = contador_no_recur + 1
        return contador_recurrente, contador_no_recur
        
hola = Ejercicio("conversiones (4).csv")
hola2 = Ejercicio("navegacion (4).csv")
hola2.cotar_usuarios()
hola.transformaciones()
hola2.recurrentes()

