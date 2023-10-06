import csv
from datetime import datetime
from collections import namedtuple

def lee_entrenos(ruta):
    with open(ruta) as datos:
        lector = csv.reader(datos)

        next(lector)

        entrenos = []

        Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            entreno = Entreno(
                tipo, 
                datetime.strptime(fechahora, "%d/%m/%Y %H:%M"), 
                ubicacion, 
                int(duracion), 
                int(calorias), 
                float(distancia),
                int(frecuencia),
                compartido == "S"
            )
            entrenos.append(entreno)
        
        return entrenos