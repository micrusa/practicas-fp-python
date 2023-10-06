from calificaciones import *
from calificaciones_ui import *

def main():
    print("### nota_teoria ###")
    print("9.1, 7.2 ==> ", nota_teoria(9.1, 7.2))
    print("4.0, 6.0 ==> ", nota_teoria(4.0, 6.0))
    print("4.0, 3.0 ==> ", nota_teoria(4.0, 3.0))
    print("None, 3.0 ==> ", nota_teoria(None, 3.0))
    print("9.0, None ==> ", nota_teoria(9.0, None))

    print("### nota_cuatrimestre ###")
    print("9.1, 7.2, 8.1 ==> ", nota_cuatrimestre((9.1, 7.2), 8.1))
    print("4.0, 6.0, 5.0 ==> ", nota_cuatrimestre((4.0, 6.0), 5.0))
    print("4.0, 3.0, None ==> ", nota_cuatrimestre((4.0, 3.0), None))
    print("None, 3.0, None ==> ", nota_cuatrimestre((None, 3.0), None))
    print("9.0, None, 4.5 ==> ", nota_cuatrimestre((9.0, None), 4.5))

    print("### nota_continua ###")
    probar_nota_continua((9.6, 9.9, 10.0, 9.8), (9.7,9.5))
    probar_nota_continua((4.4, 4.9, 5.1, 4.7), (4.6, 4.8))
    probar_nota_continua((4.0, 6.0, 4.0, 3.0), (5.0, None))
    probar_nota_continua(( 9.0, None, 4.0, 3.0), (4.5, None))

    print("### lectura_notas y nota_continua ###")
    estudiantes = lectura_notas()
    for estudiante in estudiantes:
        nota = nota_continua((estudiante.teo1, estudiante.teo2, estudiante.teo3, estudiante.teo4), (estudiante.prac1, estudiante.prac2))
        print(estudiante.uvus, " ==> ", nota)

def probar_nota_continua(notas_teoria, notas_practica):
    print("notas teoría: ", notas_teoria, " notas práctico: ", notas_practica, " ==> ", nota_continua(notas_teoria, notas_practica))

if __name__=="__main__":
    main()