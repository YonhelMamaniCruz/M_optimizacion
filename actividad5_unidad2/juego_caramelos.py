import random
from collections import Counter
import tkinter as tk
from tkinter import ttk, messagebox

CARAMEL_TYPES = ['limon', 'huevo', 'pera']

# ---------------- FUNCIONES DEL JUEGO ------------------
def can_make_chupetin(inv):
    return inv['limon'] >= 2 and inv['huevo'] >= 2 and inv['pera'] >= 2

def make_chupetin(inv, pasos):
    inv['limon'] -= 2
    inv['huevo'] -= 2
    inv['pera'] -= 2
    
    faltantes = get_faltantes_para_proxima_combinacion(inv)
    extra = []
    for dulce, cantidad in faltantes.items():
        extra.extend([dulce] * min(cantidad, 2 - len(extra)))
    while len(extra) < 2:
        extra.append(random.choice(CARAMEL_TYPES))
    inv.update(extra)

    pasos.append(f"Se hizo 1 chupetín (usando 2 limón, 2 huevo, 2 pera) y se recibieron 2 caramelos extra: {extra}")
    return 1

def vender_chupetin(inv, pasos):
    faltantes = get_faltantes_para_proxima_combinacion(inv)
    elegidos = []
    for dulce, cantidad in faltantes.items():
        elegidos.extend([dulce] * min(cantidad, 6 - len(elegidos)))
    while len(elegidos) < 6:
        elegidos.append(random.choice(CARAMEL_TYPES))
    inv.update(elegidos)

    pasos.append(f"Se vendió 1 chupetín para recibir 6 caramelos: {elegidos}")

def get_faltantes_para_proxima_combinacion(inv):
    faltan = {
        'limon': max(0, 2 - inv['limon']),
        'huevo': max(0, 2 - inv['huevo']),
        'pera': max(0, 2 - inv['pera'])
    }
    return dict(sorted(faltan.items(), key=lambda x: -x[1]))

def simular_juego():
    try:
        num_personas = int(entry_personas.get())
        tam_grupo = int(entry_grupo.get())
    except ValueError:
        messagebox.showerror("Error", "Debe ingresar números válidos.")
        return

    if num_personas <= 0 or tam_grupo <= 0:
        messagebox.showerror("Error", "Los valores deben ser mayores a cero.")
        return

    output_text.delete('1.0', tk.END)
    pasos = []

    pasos.append(f"▶ Total de personas: {num_personas}, tamaño de grupo: {tam_grupo}")
    grupos = [list(range(i, min(i + tam_grupo, num_personas))) for i in range(0, num_personas, tam_grupo)]

    for idx, grupo in enumerate(grupos):
        if len(grupo) < tam_grupo:
            pasos.append(f"⚠️ El grupo {idx+1} está incompleto con {len(grupo)} personas.")
    pasos.append("🔁 Se usará fondo común de caramelos para que todos tengan la misma oportunidad.")

    # Reparto de caramelos
    people_candies = [random.choices(CARAMEL_TYPES, k=2) for _ in range(num_personas)]
    all_candies = [c for pair in people_candies for c in pair]
    inventory = Counter(all_candies)

    pasos.append("\n📦 Reparto inicial:")
    for i, dulces in enumerate(people_candies, 1):
        pasos.append(f"Persona {i}: {dulces}")

    chupetines = 0
    intercambios = 0

    while can_make_chupetin(inventory):
        chupetines += make_chupetin(inventory, pasos)

    while chupetines < num_personas:
        if chupetines == 0:
            pasos.append("⛔ No se pueden hacer más chupetines ni vender.")
            break
        vender_chupetin(inventory, pasos)
        chupetines -= 1
        intercambios += 1
        while can_make_chupetin(inventory):
            chupetines += make_chupetin(inventory, pasos)

    pasos.append("\n📦 Inventario final de caramelos:")
    pasos.append(str(dict(inventory)))
    pasos.append(f"🍭 Chupetines totales: {chupetines}")
    pasos.append(f"🔁 Intercambios realizados: {intercambios}")

    resultado = "✅ ¡Objetivo logrado! Todos tienen al menos 1 chupetín." if chupetines >= num_personas else "❌ No se logró el objetivo."
    pasos.append("\n📌 Resultado final:")
    pasos.append(resultado)

    for linea in pasos:
        output_text.insert(tk.END, linea + "\n")

    if chupetines >= num_personas:
        messagebox.showinfo("✅ Objetivo logrado", "¡Cada persona tiene al menos un chupetín! 🎉")
    else:
        messagebox.showwarning("❌ Objetivo no logrado", "No se logró que todos tengan chupetín.")

# ---------------- INTERFAZ ------------------
root = tk.Tk()
root.title("Juego de Caramelos y Chupetines - Cooperación por Grupos")

frame = ttk.Frame(root, padding=20)
frame.pack()

title = ttk.Label(frame, text="🍬 Juego de Caramelos y Chupetines 🍭", font=("Helvetica", 16, "bold"))
title.pack()

input_frame = ttk.Frame(frame)
input_frame.pack(pady=10)

# Número de personas
ttk.Label(input_frame, text="Número de personas:").grid(row=0, column=0, padx=5)
entry_personas = ttk.Entry(input_frame, width=5)
entry_personas.insert(0, "10")
entry_personas.grid(row=0, column=1, padx=5)

# Tamaño de grupo
ttk.Label(input_frame, text="Tamaño por grupo:").grid(row=0, column=2, padx=5)
entry_grupo = ttk.Entry(input_frame, width=5)
entry_grupo.insert(0, "3")
entry_grupo.grid(row=0, column=3, padx=5)

simulate_btn = ttk.Button(frame, text="Simular Juego", command=simular_juego)
simulate_btn.pack(pady=10)

output_text = tk.Text(frame, width=90, height=35, wrap="word", font=("Courier", 10))
output_text.pack()

root.mainloop()
