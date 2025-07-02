import pandas as pd
import numpy as np

# === 1. CARGA DE DATOS ===
df_orders = pd.read_csv("order_small.csv")
df_dist = pd.read_csv("distance.csv")

print(" CARGA DE DATOS COMPLETA\n")
# === VERIFICACIÓN DE 'order_large.csv' ===

df_large = pd.read_csv("order_large.csv")

print("\n Analizando 'order_large.csv'...\n")

# Valores nulos
print(" Valores nulos en 'order_large.csv':")
print(df_large.isnull().sum())

# Duplicados
duplicados_large = df_large.duplicated().sum()
print("\n Duplicados en 'order_large.csv':", duplicados_large)

# Vista previa de columnas
print("\n Columnas:")
print(df_large.columns)

# Verificar coincidencia de IDs con distance.csv
ids_large = set(df_large['Order_ID'])
ids_dist = set(df_dist['Source']).union(set(df_dist['Destination']))
faltantes_large = ids_large - ids_dist
print("\n IDs de 'order_large.csv' que no están en 'distance.csv':", len(faltantes_large))


# === 2. LIMPIEZA BÁSICA ===

# Verificar y eliminar valores nulos
print(" Valores nulos en 'order_small.csv':")
print(df_orders.isnull().sum())
print("\n Valores nulos en 'distance.csv':")
print(df_dist.isnull().sum())

df_orders = df_orders.dropna()
df_dist = df_dist.dropna()

# Verificar y eliminar duplicados
print("\n Duplicados en 'order_small.csv':", df_orders.duplicated().sum())
print(" Duplicados en 'distance.csv':", df_dist.duplicated().sum())

df_orders = df_orders.drop_duplicates()
df_dist = df_dist.drop_duplicates()

print("\n Limpieza completada.")

# === 3. VERIFICAR Y CRUZAR IDs ===

# Usar 'Order_ID' como identificador
ids_orders = set(df_orders['Order_ID'])
ids_distance = set(df_dist['Source']).union(set(df_dist['Destination']))

ids_faltantes = ids_orders - ids_distance
print("\n IDs de 'order_small.csv' que no están en 'distance.csv':", len(ids_faltantes))

# Filtrar solo los registros de distancia que tienen IDs válidos
df_dist = df_dist[df_dist['Source'].isin(ids_orders) & df_dist['Destination'].isin(ids_orders)]

# === 4. CREAR MATRIZ DE DISTANCIAS ===

# Obtener lista única de ubicaciones
ubicaciones = pd.unique(df_orders[['Source', 'Destination']].values.ravel())
ubicaciones = sorted(ubicaciones)
ubicacion_a_indice = {loc: i for i, loc in enumerate(ubicaciones)}

# Crear matriz vacía de n x n con infinidades
n = len(ubicaciones)
matriz_dist = np.full((n, n), np.inf)

# Rellenar la matriz con valores de distancia
for _, row in df_dist.iterrows():
    i = ubicacion_a_indice[row['Source']]
    j = ubicacion_a_indice[row['Destination']]
    matriz_dist[i][j] = row['Distance(M)']
    matriz_dist[j][i] = row['Distance(M)']  # Suponemos simetría

print(f"\n Matriz de distancias construida correctamente: tamaño {n} x {n}")
