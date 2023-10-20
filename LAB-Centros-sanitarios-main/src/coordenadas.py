from collections import namedtuple;
import math as math

Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')

def calcular_distancia(coordenada1, coordenada2):
    vector = (coordenada2[0] - coordenada1[0], coordenada2[1] - coordenada1[1])
    return math.sqrt(math.pow(vector[0], 2) + math.pow(vector[1], 2))

def calcular_media_coordenadas(lista_coordenadas):
    suma_latitudes = 0.0
    suma_longitudes = 0.0
    for coordenadas in lista_coordenadas:
        suma_latitudes += coordenadas.latitud
        suma_longitudes += coordenadas.longitud
    latitud_media = suma_latitudes / len(lista_coordenadas)
    longitud_media = suma_longitudes / len(lista_coordenadas)
    return Coordenadas(latitud_media, longitud_media)