import matplotlib.pyplot as plt
import seaborn as sns

# Estilo general
sns.set(style="whitegrid", context="notebook")

# Datos de ejemplo
etiquetas = ['Ruta Aleatoria', 'Ruta Evolutiva']
distancias = [73593576.9, 34892902.0]
diferencia = distancias[0] - distancias[1]

# Crear figura con 1 fila y 2 columnas
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: gráfico de líneas con puntos
axs[0].plot(etiquetas, distancias, marker='o', markersize=10, linewidth=2.5, color='royalblue')
axs[0].set_title("Distancia Total por Método", fontsize=14, fontweight='bold')
axs[0].set_ylabel("Distancia Total (m)")
axs[0].set_ylim(min(distancias) * 0.9, max(distancias) * 1.05)

# Etiquetas de valor
for i, val in enumerate(distancias):
    axs[0].text(i, val + 1_000_000, f"{val:,.0f}", ha='center', va='bottom', fontsize=10)

# Subplot 2: línea horizontal con anotación
axs[1].hlines(y=0.5, xmin=distancias[1], xmax=distancias[0], color='darkgreen', linewidth=4)
axs[1].plot(distancias[0], 0.5, 'o', color='royalblue', label='Aleatoria')
axs[1].plot(distancias[1], 0.5, 'o', color='orangered', label='Evolutiva')

axs[1].text(distancias[1], 0.52, 'Evolutiva', ha='right', fontsize=10)
axs[1].text(distancias[0], 0.52, 'Aleatoria', ha='left', fontsize=10)
axs[1].text((distancias[0]+distancias[1])/2, 0.53, f"Mejora: {diferencia:,.0f} m",
            ha='center', fontsize=11, fontweight='bold', color='darkgreen')

axs[1].set_ylim(0, 1)
axs[1].set_yticks([])
axs[1].set_title("Reducción de Distancia", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Distancia Total (m)")

# Ajuste final
plt.tight_layout()
plt.savefig("comparacion_rutas_mejorado.png", dpi=300)
plt.show()

