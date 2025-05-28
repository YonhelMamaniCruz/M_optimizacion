import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import ElasticNet
import optuna

# Carga y preprocesamiento (como tú hiciste)
df = pd.read_csv('data_residuos.csv', sep=';', encoding='latin1')
df.columns = df.columns.str.replace(' ', '_')

columnas_categoricas = ['DEPARTAMENTO', 'PROVINCIA', 'DISTRITO',
                       'REGION_NATURAL', 'TIPO_MUNICIPALIDAD', 'CLASIFICACION_MUNICIPAL_MEF']

le = LabelEncoder()
for col in columnas_categoricas:
    df[col] = le.fit_transform(df[col])

X = df.drop(columns=['GENERACION_PER_CAPITA_MUNICIPAL'])
y = df['GENERACION_PER_CAPITA_MUNICIPAL']

# Escalado (importante para ElasticNet)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Función objetivo para Optuna
def objective(trial):
    alpha = trial.suggest_float('alpha', 1e-5, 10.0, log=True)
    l1_ratio = trial.suggest_float('l1_ratio', 0.0, 1.0)
    
    model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42, max_iter=10000)
    # Validación cruzada para evaluar el modelo (neg_mean_squared_error)
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
    rmse = (-scores.mean()) ** 0.5
    return rmse

# Crear estudio y optimizar
study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=50)

print("Mejores hiperparámetros:", study.best_params)
print("Mejor RMSE en CV:", study.best_value)

# Entrenar el modelo final con mejores hiperparámetros
best_model = ElasticNet(**study.best_params, random_state=42, max_iter=10000)
best_model.fit(X_train, y_train)

from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

y_pred = best_model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"RMSE en test: {rmse:.4f}")
print(f"R2 en test: {r2:.4f}")
#----------------------------------------------------------------------

from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Modelo sin optimización (por defecto)
model_default = ElasticNet(random_state=42, max_iter=10000)
model_default.fit(X_train, y_train)
y_pred_default = model_default.predict(X_test)
rmse_default = np.sqrt(mean_squared_error(y_test, y_pred_default))
r2_default = r2_score(y_test, y_pred_default)

# Modelo con parámetros optimizados por Optuna
best_model = ElasticNet(**study.best_params, random_state=42, max_iter=10000)
best_model.fit(X_train, y_train)
y_pred_opt = best_model.predict(X_test)
rmse_opt = np.sqrt(mean_squared_error(y_test, y_pred_opt))
r2_opt = r2_score(y_test, y_pred_opt)

# Mostrar resultados
print("==== Comparación de modelos ElasticNet ====")
print(f"Sin optimización - RMSE: {rmse_default:.4f}, R²: {r2_default:.4f}")
print(f"Con Optuna     - RMSE: {rmse_opt:.4f}, R²: {r2_opt:.4f}")
#------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

metrics = ['RMSE', 'R2']
default_vals = [rmse_default, r2_default]
optuna_vals = [rmse_opt, r2_opt]

x = range(len(metrics))

plt.bar(x, default_vals, width=0.4, label='Sin optimización', align='center')
plt.bar([i + 0.4 for i in x], optuna_vals, width=0.4, label='Con Optuna', align='center')
plt.xticks([i + 0.2 for i in x], metrics)
plt.title("Comparación métricas ElasticNet antes y después de Optuna")
plt.legend()
plt.show()
