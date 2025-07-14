import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar matriz de distancias
df_dist = pd.read_csv("distance.csv")
ubicaciones = sorted(set(df_dist["Source"].unique()) | set(df_dist["Destination"].unique()))
ubicacion_a_indice = {u: i for i, u in enumerate(ubicaciones)}
n = len(ubicaciones)

# Construir matriz de distancias
matriz = np.full((n, n), np.inf)
for _, fila in df_dist.iterrows():
    i = ubicacion_a_indice[fila["Source"]]
    j = ubicacion_a_indice[fila["Destination"]]
    matriz[i][j] = fila["Distance(M)"]
    matriz[j][i] = fila["Distance(M)"]  # Asumimos simetría

# Función para calcular la distancia total de una ruta
def evaluar(ruta):
    distancia = 0
    for i in range(len(ruta) - 1):
        a = ubicacion_a_indice[ruta[i]]
        b = ubicacion_a_indice[ruta[i + 1]]
        distancia += matriz[a][b]
    return distancia

# Operadores genéticos
def seleccionar_padres(poblacion, distancias, k=3):
    padres = []
    for _ in range(len(poblacion)):
        torneo = random.sample(list(zip(poblacion, distancias)), k)
        ganador = min(torneo, key=lambda x: x[1])[0]
        padres.append(ganador)
    return padres

def cruce_ordenado(padre1, padre2):
    a, b = sorted(random.sample(range(len(padre1)), 2))
    hijo = [None] * len(padre1)
    hijo[a:b] = padre1[a:b]
    p2 = [ciudad for ciudad in padre2 if ciudad not in hijo[a:b]]
    j = 0
    for i in range(len(hijo)):
        if hijo[i] is None:
            hijo[i] = p2[j]
            j += 1
    return hijo

def mutacion(ruta, tasa=0.1):
    nueva_ruta = ruta[:]
    if random.random() < tasa:
        i, j = random.sample(range(len(nueva_ruta)), 2)
        nueva_ruta[i], nueva_ruta[j] = nueva_ruta[j], nueva_ruta[i]
    return nueva_ruta

# Algoritmo evolutivo
def algoritmo_evolutivo(ubicaciones, generaciones=100, tam_poblacion=50):
    poblacion = [random.sample(ubicaciones, len(ubicaciones)) for _ in range(tam_poblacion)]
    mejor_ruta = None
    mejor_distancia = float("inf")
    historia = []

    for gen in range(generaciones):
        distancias = [evaluar(ruta) for ruta in poblacion]
        padres = seleccionar_padres(poblacion, distancias)
        nueva_poblacion = []

        for i in range(0, len(padres), 2):
            if i + 1 < len(padres):
                hijo1 = cruce_ordenado(padres[i], padres[i + 1])
                hijo2 = cruce_ordenado(padres[i + 1], padres[i])
                nueva_poblacion.append(mutacion(hijo1))
                nueva_poblacion.append(mutacion(hijo2))

        poblacion = nueva_poblacion
        distancias = [evaluar(ruta) for ruta in poblacion]
        mejor_gen = min(zip(poblacion, distancias), key=lambda x: x[1])

        if mejor_gen[1] < mejor_distancia:
            mejor_ruta, mejor_distancia = mejor_gen

        historia.append(mejor_distancia)

    return mejor_ruta, mejor_distancia, historia

# Ejecutar el algoritmo
mejor_ruta, mejor_distancia, historia = algoritmo_evolutivo(ubicaciones, generaciones=100)

print("Mejor distancia evolutiva:", mejor_distancia)
print("Ruta:", mejor_ruta)

# Gráfica de convergencia
plt.plot(historia)
plt.title("Mejora de la distancia por generación")
plt.xlabel("Generación")
plt.ylabel("Distancia total")
plt.grid()
plt.tight_layout()
plt.savefig("evolutivo_convergencia.png")
plt.show()
