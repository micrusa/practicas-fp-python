import csv
from collections import namedtuple

def lectura_notas():
    RegistroNotas = namedtuple('RegistroNotas', 'uvus, teo1, teo2, prac1, teo3, teo4,prac2 ')
    registros = []
    with open("data/notas.csv") as datos:
        lector = csv.reader(datos)

        next(lector)

        for uvus, t1, t2, p1, t3, t4, p2 in lector:
            teo1 = procesar_nota(t1)
            teo2 = procesar_nota(t2)
            prac1 = procesar_nota(p1)
            teo3 = procesar_nota(t3)
            teo4 = procesar_nota(t4)
            prac2 = procesar_nota(p2)
            registros.append(RegistroNotas(uvus, teo1, teo2, prac1, teo3, teo4, prac2))

    return registros

def procesar_nota(nota):
    nota_final = None
    if nota != "-":
        nota_final = float(nota)
    return nota_final
