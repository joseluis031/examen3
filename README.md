# examen3

El link del repositorio es: https://github.com/joseluis031/examen3.git

## El codigo del main es

```
if __name__ == "__main__":
    from Clases.ejercicio import *
    hola = Ejercicio("conversiones (4).csv")
    hola2 = Ejercicio("navegacion (4).csv")
    hola.transformaciones()
    hola2.recurrentes()
    hola2.repetidos()
    hola2.coche_mas_visto()
    
    
    from Clases.graficass import *
    
    hola2 = Graficas("navegacion (4).csv")
    hola3 = Graficas("conversiones (4).csv")
    print(hola2.histograma_url_landing())
    print(hola3.histograma_user_recurrent())
    print(hola3.histograma_lead_type())
    
   ```
