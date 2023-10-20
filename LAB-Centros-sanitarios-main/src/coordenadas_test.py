from collections import namedtuple
from coordenadas import *

def main():
    lista_coordenadas_prueba = [Coordenadas(1.0, 7.4), Coordenadas(0.2, 4.3), Coordenadas(0.7, 0.9), Coordenadas(0.2, 0.5), Coordenadas(0.9,3.5)]
    assert len(lista_coordenadas_prueba) >= 2
    for i in range(int(len(lista_coordenadas_prueba)/2)):
        coordenada1 = lista_coordenadas_prueba[i]
        coordenada2 = lista_coordenadas_prueba[i+1]
        print("distancia de ", coordenada1, "y", coordenada2, ": ", calcular_distancia(coordenada1, coordenada2))

    print("media de ", lista_coordenadas_prueba, ": ", calcular_media_coordenadas(lista_coordenadas_prueba))

if __name__ == '__main__':
    main()