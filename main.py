if __name__ == "__main__":
    from Clases.ejercicio import *
    hola = Ejercicio("conversiones (4).csv")
    hola2 = Ejercicio("navegacion (4).csv")
    hola.transformaciones()
    hola2.recurrentes()
    hola2.repetidos()
    hola2.coche_mas_visto()