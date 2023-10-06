def mayorDuracionEnAno(entrenos, ano):
    max = entrenos[0]
    for entreno in entrenos:
        if entreno.fechahora.year == ano and entreno.duracion > max.duracion:
            max = entreno
    return max

def ciudadesPorTipo(entrenos, tipo):
    ciudades = []
    for entreno in entrenos:
        if entreno.tipo == tipo and not entreno.ubicacion in ciudades:
            ciudades.append(entreno.ubicacion)
    return ciudades

def kmRecorridos(entrenos, ciudades):
    kmTotales = 0
    for entreno in entrenos:
        if entreno.ubicacion in ciudades:
            kmTotales += entreno.distancia
    return kmTotales

def horaConMasEntrenos(entrenos, hora1, hora2):
    entrenosHora1 = 0
    entrenosHora2 = 0
    for entreno in entrenos:
        if entreno.fechahora.hour == hora1:
            entrenosHora1 += 1
        elif entreno.fechahora.hour == hora2:
            entrenosHora2 += 1
    if hora1 > hora2:
        horaMasEntrenos = hora1
    elif hora2 > hora1:
        horaMasEntrenos = hora2
    return horaMasEntrenos