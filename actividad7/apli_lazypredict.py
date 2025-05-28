import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

# Configuración para gráficos más bonitos
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
import pandas as pd
from lazypredict.Supervised import LazyRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Leer el dataset
df = pd.read_csv('data_residuos.csv', sep=';', encoding='latin1')

# Reemplazar espacios en nombres de columnas
df.columns = df.columns.str.replace(' ', '_')

# Opcional: codificar columnas categóricas
columnas_categoricas = ['DEPARTAMENTO', 'PROVINCIA', 'DISTRITO',
                        'REGION_NATURAL', 'TIPO_MUNICIPALIDAD', 'CLASIFICACION_MUNICIPAL_MEF']

le = LabelEncoder()
for col in columnas_categoricas:
    df[col] = le.fit_transform(df[col])

# Seleccionar variables predictoras y variable objetivo
X = df.drop(columns=['GENERACION_PER_CAPITA_MUNICIPAL'])  # variables independientes
y = df['GENERACION_PER_CAPITA_MUNICIPAL']  # variable objetivo

# Separar en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# LazyPredict
reg = LazyRegressor(verbose=0, ignore_warnings=True, custom_metric=None)
models, predictions = reg.fit(X_train, X_test, y_train, y_test)

# Mostrar resultados
print("\n📊 Modelos ordenados por desempeño:\n")
print(models)
