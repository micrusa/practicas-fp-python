def nones_a_0(valor):
    if valor == None:
        return 0
    else:
        return valor

def nota_teoria(media1, media2):
    nota1 = nones_a_0(media1)
    nota2 = nones_a_0(media2)
    return (nota1 + nota2) / 2

def nota_cuatrimestre(notas_teoricas, nota_practico):
    practico = nones_a_0(nota_practico)
    media_teoricos = nota_teoria(notas_teoricas[0], notas_teoricas[1])
    if media_teoricos > 4:
        nota_final = 0.2 * media_teoricos + 0.8 * practico
    else:
        nota_final = 0
    return nota_final

def nota_continua(notas_teoricas, notas_practicas):
    nota_primer_cuatrimestre = nota_cuatrimestre(notas_teoricas[0:2], notas_practicas[0])
    nota_segundo_cuatrimestre = nota_cuatrimestre(notas_teoricas[2:4], notas_practicas[1])
    nota_final = (nota_primer_cuatrimestre + nota_segundo_cuatrimestre) / 2
    if nota_primer_cuatrimestre < 4 or nota_segundo_cuatrimestre < 4:
        nota_final = min(4, nota_final)
    return nota_final
