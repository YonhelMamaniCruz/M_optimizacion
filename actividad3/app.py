from flask import Flask, render_template, request
app = Flask(__name__)

def gauss_jordan(matriz):
    n = len(matriz)
    for i in range(n):
        pivote = matriz[i][i]
        if pivote == 0:
            raise ValueError("División por cero. Sistema no resoluble.")
        for j in range(n + 1):
            matriz[i][j] /= pivote
        for k in range(n):
            if k != i:
                factor = matriz[k][i]
                for j in range(n + 1):
                    matriz[k][j] -= factor * matriz[i][j]
    return [round(matriz[i][-1], 4) for i in range(n)]

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = []
    n = 0
    matriz = []

    if request.method == 'POST':
        n = int(request.form['n'])
        matriz = []
        try:
            for i in range(n):
                fila = []
                for j in range(n + 1):
                    campo = f"v_{i}_{j}"
                    fila.append(float(request.form[campo]))
                matriz.append(fila)
            resultado = gauss_jordan(matriz)
        except Exception as e:
            resultado = [f"Error: {e}"]

    return render_template('index.html', n=n, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
