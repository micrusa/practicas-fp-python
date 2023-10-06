from entrenos_lectura import *
from entrenos_funciones import *

def main():
    entrenos = lee_entrenos("data/entrenos.csv")
    print("### Primeros y ultimos 3 entrenos ###")
    for i in range(3):
        if len(entrenos) > i:
            print(i, " => ", entrenos[i])
    for i in range(3):
        indice = len(entrenos) + i - 4
        if indice >= 0:
            print(indice, " => ", entrenos[indice])

    print("### Entreno de mayor duracion en años ###")
    for i in range(3):
        ano = 2019 + i
        print(ano, " => ", mayorDuracionEnAno(entrenos, ano))

    print("### Ciudades por tipo y km recorridos en dichas ciudades ###")
    for tipo in ["Remo", "Andar", "Bici", "Elíptica", "Senderismo", "Yoga", "Cinta"]:
        ciudades = ciudadesPorTipo(entrenos, tipo)
        print(tipo, " => ", ciudades, "(", kmRecorridos(entrenos, ciudades), "km )")

    print("### Hora con mas entrenos ###")
    for horas in [[11, 12], [17, 10]]:
        print(horas, " => ", horaConMasEntrenos(entrenos, horas[0], horas[1]))
    

if __name__ == "__main__":
    main()