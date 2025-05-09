def gauss_jordan(matriz):
    n = len(matriz)

    for i in range(n):
        # Hacer que el pivote sea 1
        pivote = matriz[i][i]
        if pivote == 0:
            raise ValueError("No se puede dividir entre cero. El sistema puede no tener solución única.")
        for j in range(n + 1):
            matriz[i][j] = matriz[i][j] / pivote

        # Hacer ceros en las otras filas
        for k in range(n):
            if k != i:
                factor = matriz[k][i]
                for j in range(n + 1):
                    matriz[k][j] -= factor * matriz[i][j]

    # Extraer soluciones
    soluciones = [matriz[i][-1] for i in range(n)]
    return soluciones



n = int(input("Ingrese el número de ecuaciones (y de incógnitas): "))

print(f"\nIngrese los coeficientes de cada ecuación (incluya el término independiente):")
print(f"Formato: a1 a2 ... an b (separados por espacio)")

matriz = []
for i in range(n):
    fila = list(map(float, input(f"Ecuación {i+1}: ").split()))
    if len(fila) != n + 1:
        print("Error: debe ingresar exactamente", n + 1, "valores.")
        exit()
    matriz.append(fila)

try:
    soluciones = gauss_jordan(matriz)
    print("\nSoluciones:")
    for i, valor in enumerate(soluciones):
        print(f"x{i+1} = {round(valor, 4)}")
except Exception as e:
    print("Error:", str(e))
