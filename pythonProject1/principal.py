import os.path
from registro import *


def mostrar_menu():
    print("-" * 80)
    print("CATALOGO DE SERIES")
    print("1. Mostrar Vector")
    print("2. Generar archivo por idioma.")
    print("3. Buscar por titulo.")
    print("4. Duracion de series en español por genero.")
    print("5. Contar por genero e idioma.")
    print("0. Salir.")
    print("-" * 80)


def mostrar_vector(v):
    pass


def leer_archivo_csv(fd):
    v = list()
    if os.path.exists(fd):
        m = open(fd, 'rt')
        for linea in m:
            reg = csv_to_Serie(linea)
            v.append(reg)
        m.close()
    else:
        print("El archivo no existe")


def ordenar_por_titulo(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i + 1, n):
            if v[i].titulo > v[j].titulo:
                v[i], v[j] = v[j], v[i]


def principal():
    fd = 'series.csv'
    v = leer_archivo_csv(fd)
    if len(v) == 0:
        return

    ordenar_por_titulo(v)
    opcion = -1
    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Ingrese su opcion: "))

        if opcion == 1:
            #Listar contenido del vector, mostrando una linea por serie.
            mostrar_vector(v)

principal()
