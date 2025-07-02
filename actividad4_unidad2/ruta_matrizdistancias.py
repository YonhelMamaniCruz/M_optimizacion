import pandas as pd
import numpy as np
import random

# Cargar datos
df_orders = pd.read_csv("order_small.csv")
df_dist = pd.read_csv("distance.csv")

# Extraer ubicaciones únicas
ubicaciones = list(set(df_dist['Source']).union(set(df_dist['Destination'])))
ubicaciones.sort()
ubicacion_a_indice = {ubicacion: i for i, ubicacion in enumerate(ubicaciones)}


# Crear índice para acceder a la matriz
ubicacion_a_indice = {ubicacion: i for i, ubicacion in enumerate(ubicaciones)}

# Construcción de la matriz de distancias
n = len(ubicaciones)
matriz_dist = np.zeros((n, n))

for _, row in df_dist.iterrows():
    origen = row['Source']
    destino = row['Destination']
    dist = row['Distance(M)']
    i = ubicacion_a_indice[origen]
    j = ubicacion_a_indice[destino]
    matriz_dist[i][j] = dist
    matriz_dist[j][i] = dist  # Asumimos simetría

#ruta aleatoria y calculo de distancia
def generar_ruta_aleatoria(nodos):
    ruta = nodos.copy()
    random.shuffle(ruta)
    return ruta

def calcular_distancia_total(ruta, matriz, indices):
    total = 0
    for i in range(len(ruta) - 1):
        origen = indices[ruta[i]]
        destino = indices[ruta[i + 1]]
        total += matriz[origen][destino]
    return total

#generar rutas aleatorias y comparar
rutas = []
distancias = []

for _ in range(100):
    ruta = generar_ruta_aleatoria(ubicaciones)
    distancia = calcular_distancia_total(ruta, matriz_dist, ubicacion_a_indice)
    rutas.append(ruta)
    distancias.append(distancia)

print("Distancia promedio (aleatorias):", np.mean(distancias))
print("Mejor ruta aleatoria:", rutas[np.argmin(distancias)])
print("Distancia mínima:", min(distancias))
