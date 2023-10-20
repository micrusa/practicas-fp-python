from collections import namedtuple
import csv
from coordenadas import *
from mapas import *

def leer_centros(ruta):
    with open(ruta) as archivo:
        datos = csv.reader(archivo, delimiter=";")
        
        next(datos)

        CentroSanitario = namedtuple('CentroSanitario', 'nombre, localidad, coordenadas, estado, num_camas, acceso_minusvalidos, tiene_uci')

        centros = []

        for nombre, localidad, latitud, longitud, estado, num_camas, acceso_minusvalidos, tiene_uci in datos:
            # Usamos strip para eliminar espacios al principio y al final, porque estan divididos por "; ", no ";"
            coordenadas = Coordenadas(float(latitud.strip()), float(longitud.strip()))
            centro = CentroSanitario(
                nombre.strip(),
                localidad.strip(), 
                coordenadas, 
                estado.strip(), 
                int(num_camas.strip()),
                # al estar en minúsculas bool() no lo lee correctamente, usamos == "true"
                acceso_minusvalidos.strip() == "true",
                tiene_uci.strip() == "true"
                )
            centros.append(centro)

        return centros

def calcular_total_camas_centros_accesibles(centros):
    num_camas = 0
    for centro in centros:
        if centro.acceso_minusvalidos:
            num_camas += centro.num_camas

    return num_camas

def obtener_centros_con_uci_cercanos_a(centros, coordenadas, umbral):
    centros_cercanos = []
    for centro in centros:
        if centro.tiene_uci and calcular_distancia(coordenadas, centro.coordenadas) <= umbral:
            tupla_centro = (centro.nombre, centro.localidad, centro.coordenadas)
            centros_cercanos.append(tupla_centro)

    return centros_cercanos

def generar_mapa(centros, ruta):
    mapa = crea_mapa(calcular_media_coordenadas(list(map(lambda centro : centro[2], centros))))
    for centro in centros:
        agrega_marcador(mapa, centro[2], centro[0], 'red')
    
    guarda_mapa(mapa, ruta)