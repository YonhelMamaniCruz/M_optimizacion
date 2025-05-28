
import pandas as pd

# 1. Cargar el archivo CSV
df = pd.read_csv('data_residuos.csv', sep=';', encoding='latin1')


# 2. Mostrar primeras filas
print("Primeras filas del dataset:")
print(df.head())
print("🔎 Valores nulos por columna:\n")
print(df.isnull().sum())
# 3. Revisar tipos de datos
print("\nTipos de datos:")
print(df.dtypes)
duplicados = df.duplicated().sum()
print(f"🔁 Filas duplicadas: {duplicados}")

