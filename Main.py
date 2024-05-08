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

