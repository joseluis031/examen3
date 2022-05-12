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
        self.A = self.datos["uuid"].count()
        


    def transformaciones(self): #con esta funcion se cuenta cuantos clientes finalmente han realizado la conversion con un bucle
        contador_call = 0  
        contador_form = 0
        for i in self.datos["lead_type"]:
            if i == "CALL":
                contador_call = contador_call + 1
            elif i =="FORM":
                contador_form = contador_form + 1
        return contador_call, contador_form
    def recurrentes(self): # funcion para tipo de reccurrencia
        contador_recurrente = 0
        contador_no_recur = 0
        for i in self.datos["user_recurrent"]:
            if i == "True":
                contador_recurrente = contador_recurrente + 1
            elif i == "False":
                contador_no_recur = contador_no_recur + 1
        return ((contador_recurrente/self.A)*100, (contador_no_recur/self.A)*100)
    
    def repetidos(self):
        self.B = self.datos["id_user"].drop_duplicates()
        self.C = self.datos["gclid"].drop_duplicates()
        return self.B, self.A
    def coche_mas_visto(self):
        indice= self.datos.loc[self.datos[0]==self.cant].index
        valor = self.datos["url_landing"][indice][0]
        return valor


