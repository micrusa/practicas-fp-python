from centros import *
from coordenadas import Coordenadas

def main():
    centros = leer_centros("data/centrosSanitarios.csv")
    
    print("Camas accesibles: ", calcular_total_camas_centros_accesibles(centros))
    coordenada_test = Coordenadas(36.17809045129006, -5.378933716676538)
    centros_cercanos = obtener_centros_con_uci_cercanos_a(centros, coordenada_test, 0.1)
    print("Centros cercanos a ", coordenada_test, ": ", centros_cercanos)
    ruta = "test.html"
    generar_mapa(centros_cercanos, ruta)
    print("mapa generado en ", ruta)

if __name__ == "__main__":
    main()