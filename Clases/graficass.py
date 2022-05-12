import matplotlib.pyplot as plt
import pandas as pd





class Graficas:
    def __init__(self,datos):
        self.datos = pd.read_csv(datos)
    def histograma_lead_type(self):
        fig, ax = plt.subplots()
# Filtramos los distritos de la lista de distritos dada, después contamos la frecuencias de los tipos de alojamientos y dibujamos el diagrama de sectores
        self.datos["lead_type"].plot(kind = 'hist', ax = ax)
# Ponermos el título
        ax.set_title('lead_type', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
# Eliminamos la etiqueta del eje y
        ax.set_ylabel('')
# Guardamos el gráfico.
        plt.savefig('Graficos/histograma_lead_type.png', bbox_inches='tight')
        return plt.show()
    
    def histograma_user_recurrent(self):
        fig, ax = plt.subplots()
# Filtramos los distritos de la lista de distritos dada, después contamos la frecuencias de los tipos de alojamientos y dibujamos el diagrama de sectores
        self.datos["user_recurrent"].plot(kind = 'hist', ax = ax)
# Ponermos el título
        ax.set_title('user_recurrent', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
# Eliminamos la etiqueta del eje y
        ax.set_ylabel('')
# Guardamos el gráfico.
        plt.savefig('Graficos/histograma_user_recurrent.png', bbox_inches='tight')
        return plt.show()
    
    def histograma_url_landing(self):
        fig, ax = plt.subplots()
# Filtramos los distritos de la lista de distritos dada, después contamos la frecuencias de los tipos de alojamientos y dibujamos el diagrama de sectores
        self.datos["url_landing"].plot(kind = 'hist', ax = ax)
# Ponermos el título
        ax.set_title('url_landing', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
# Eliminamos la etiqueta del eje y
        ax.set_ylabel('')
# Guardamos el gráfico.
        plt.savefig('Graficos/histograma_url_landing.png', bbox_inches='tight')
        return plt.show()
    
