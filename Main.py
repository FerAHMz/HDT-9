#Fernando Hernandez-23645
#Nicolás Concua-23197
#Hoja de trabajo 9
#Algoritmo de Dijkstra

import networkx as nx
import matplotlib.pyplot as plt

def cargarRutas(archivo):
    grafo = nx.Graph()
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.replace('“', '"').replace('”', '"')
            datos = linea.strip().split(', ')
            origen = datos[0].strip('"').strip("'")
            destino = datos[1].strip('"').strip("'")
            costo = int(datos[2])
            grafo.add_edge(origen, destino, weight=costo)
    return grafo

Grafo = cargarRutas("rutas.txt")

def RutasOrigen(Grafo, cliente):
    rutas, costos = nx.single_source_dijkstra(Grafo, cliente)
    for destino, costo in costos.items():
        print(f"Destino: {destino}, Costo: {costo}, Ruta: {rutas[destino]}")

#Ciclo while para que el usuario pueda ingresar las rutas que desee
while True:
    print(f"Estaciones disponibles: {Grafo.nodes()}")
    cliente=input("Ingrese el nombre de su estacion de salida: ")
    RutasOrigen(Grafo, cliente)
    nx.draw(Grafo, with_labels=True)
    plt.show()
    print("Desea seguir consultando rutas?")
    print("1. Si")
    print("2. No")
    continuar=input()
    if continuar=="1":
        continue
    else:
        break

