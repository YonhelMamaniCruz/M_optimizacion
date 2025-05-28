import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# Estilo del gráfico
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

# Datos reales (Horas de estudio vs Calificación)
x_datos = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y_datos = np.array([50, 55, 65, 70, 75, 85, 88, 92])

# Parámetros de la línea de regresión propuesta
m_prueba = 6
b_prueba = 45

# Predicción con la línea propuesta
y_prediccion = m_prueba * x_datos + b_prueba

# Calcular el error cuadrático medio (ECM)
mse = mean_squared_error(y_datos, y_prediccion)
print(f"Error cuadrático medio (ECM): {mse:.2f}")

# Visualización
plt.figure(figsize=(12, 8))
plt.scatter(x_datos, y_datos, s=100, alpha=0.7, label='Datos reales', zorder=5)
plt.plot(x_datos, y_prediccion, 'ro', markersize=8, label='Predicciones', zorder=4)

# Línea continua de la recta propuesta
x_linea = np.linspace(min(x_datos), max(x_datos), 100)
y_linea = m_prueba * x_linea + b_prueba
plt.plot(x_linea, y_linea, 'r-', linewidth=2, alpha=0.7,
         label=f'Línea propuesta: y = {m_prueba}x + {b_prueba}')

# Dibujar líneas de error
for i in range(len(x_datos)):
    plt.plot([x_datos[i], x_datos[i]], [y_datos[i], y_prediccion[i]],
             'k-', linewidth=1, alpha=0.5)

    # Anotar algunos errores
    if i % 5 == 0:
        error = y_datos[i] - y_prediccion[i]
        plt.annotate(f'error = {error:.1f}',
                     (x_datos[i], (y_datos[i] + y_prediccion[i]) / 2),
                     xytext=(10, 0), textcoords='offset points',
                     fontsize=9, alpha=0.7)

# Etiquetas y leyenda
plt.xlabel('Horas de estudio')
plt.ylabel('Calificación')
plt.title('Visualización de los Errores de Predicción')
plt.legend()
plt.tight_layout()

# Mostrar gráfico
plt.show()

# Guardar imagen (opcional)
# plt.savefig("errores_prediccion.png", dpi=300)
#--------------------------------------------------------
# Tus datos
x_datos = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y_datos = np.array([50, 55, 65, 70, 75, 85, 88, 92])

# Función para calcular regresión lineal paso a paso
import numpy as np

# Función para calcular regresión lineal paso a paso
def calcular_regresion_lineal(x, y, mostrar_pasos=True):
    """
    Calcula los coeficientes de regresión lineal (pendiente y ordenada al origen)
    utilizando el método de mínimos cuadrados. Muestra los pasos si se desea.
    
    Parámetros:
        x (array-like): Valores independientes.
        y (array-like): Valores dependientes.
        mostrar_pasos (bool): Si True, muestra los pasos del cálculo.

    Retorna:
        m (float): Pendiente.
        b (float): Intercepto.
    """
    x = np.array(x)
    y = np.array(y)

    if len(x) != len(y):
        raise ValueError("x e y deben tener la misma longitud")

    n = len(x)

    # Paso 1: Calcular las medias
    x_media = np.mean(x)
    y_media = np.mean(y)

    if mostrar_pasos:
        print("=== PASO 1: Calcular las medias ===")
        print(f"x̄ = Σx/n = {np.sum(x):.2f}/{n} = {x_media:.2f}")
        print(f"ȳ = Σy/n = {np.sum(y):.2f}/{n} = {y_media:.2f}")

    # Paso 2: Calcular las diferencias respecto a las medias
    x_diff = x - x_media
    y_diff = y - y_media

    if mostrar_pasos:
        print("\n=== PASO 2: Calcular diferencias respecto a la media ===")
        print("Primeros 5 valores:")
        for i in range(min(5, n)):
            print(f"x[{i}] - x̄ = {x[i]:.2f} - {x_media:.2f} = {x_diff[i]:.2f}")
            print(f"y[{i}] - ȳ = {y[i]:.2f} - {y_media:.2f} = {y_diff[i]:.2f}")

    # Paso 3: Calcular sumatorias necesarias
    suma_xy = np.sum(x_diff * y_diff)
    suma_xx = np.sum(x_diff ** 2)

    if mostrar_pasos:
        print(f"\n=== PASO 3: Calcular sumas ===")
        print(f"Σ(x - x̄)(y - ȳ) = {suma_xy:.2f}")
        print(f"Σ(x - x̄)² = {suma_xx:.2f}")

    # Paso 4: Calcular pendiente (m)
    m = suma_xy / suma_xx

    if mostrar_pasos:
        print(f"\n=== PASO 4: Calcular la pendiente ===")
        print(f"m = Σ(x - x̄)(y - ȳ) / Σ(x - x̄)²")
        print(f"m = {suma_xy:.2f} / {suma_xx:.2f} = {m:.2f}")

    # Paso 5: Calcular intercepto (b)
    b = y_media - m * x_media

    if mostrar_pasos:
        print(f"\n=== PASO 5: Calcular el intercepto ===")
        print(f"b = ȳ - m * x̄")
        print(f"b = {y_media:.2f} - {m:.2f} * {x_media:.2f} = {b:.2f}")

    return m, b

# === Datos ===
x_datos = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y_datos = np.array([50, 55, 65, 70, 75, 85, 88, 92])

# Ejecutar la función
print("ENCONTRANDO LOS MEJORES COEFICIENTES")
print("=" * 50)
m_optimo, b_optimo = calcular_regresion_lineal(x_datos, y_datos)
print("\nResultado final:")
print(f"Pendiente óptima (m): {m_optimo:.2f}")
print(f"Intercepto óptimo (b): {b_optimo:.2f}")
