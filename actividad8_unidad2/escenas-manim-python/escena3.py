from manim import *
import numpy as np
import random

class AlgoritmoGenetico(Scene):
    def construct(self):
        # Título principal
        titulo = Text("Algoritmo Genético para Optimización de Rutas", 
                     font_size=28, weight=BOLD, color=GREEN)
        titulo.to_edge(UP, buff=0.5)
        
        self.play(Write(titulo), run_time=2)
        
        # Subtítulo técnico
        subtitulo = Text("Implementación basada en principios de evolución biológica", 
                        font_size=16, color=BLUE)
        subtitulo.next_to(titulo, DOWN, buff=0.3)
        
        self.play(Write(subtitulo), run_time=1.5)
        self.wait(1)
        
        # SECCIÓN 1: FUNCIÓN OBJETIVO DEL TSP
        self.play(FadeOut(subtitulo))
        
        seccion_objetivo = Text("Función Objetivo del Problema TSP", 
                               font_size=20, weight=BOLD, color=ORANGE)
        seccion_objetivo.to_edge(LEFT, buff=1).shift(UP * 2.5)
        
        self.play(Write(seccion_objetivo))
        
        # Fórmula principal del TSP (Ecuación 1 de su artículo)
        formula_tsp = MathTex(
            r"f(x) = \sum_{i=1}^{n-1} d(x_i, x_{i+1}) + d(x_n, x_1)",
            font_size=24, color=WHITE
        )
        formula_tsp.next_to(seccion_objetivo, DOWN, buff=0.5)
        
        self.play(Write(formula_tsp), run_time=2)
        
        # Explicación de variables
        explicacion_vars = VGroup(
            Text("donde:", font_size=14, color=WHITE),
            Text("x = permutación de ciudades", font_size=12, color=WHITE),
            Text("d(xi, xi+1) = distancia entre nodos consecutivos", font_size=12, color=WHITE),
            Text("n = número total de ciudades", font_size=12, color=WHITE)
        )
        explicacion_vars.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explicacion_vars.next_to(formula_tsp, DOWN, buff=0.4)
        
        self.play(Write(explicacion_vars), run_time=2.5)
        self.wait(2)
        
        # Transición a componentes del algoritmo
        self.play(FadeOut(VGroup(seccion_objetivo, formula_tsp, explicacion_vars)))
        
        # SECCIÓN 2: COMPONENTES DEL ALGORITMO GENÉTICO
        componentes_titulo = Text("Componentes del Algoritmo Genético", 
                                 font_size=20, weight=BOLD, color=PURPLE)
        componentes_titulo.to_edge(UP, buff=1)
        
        self.play(Transform(titulo, componentes_titulo))
        
        # Lista de operadores (basada en su implementación exacta)
        operadores = VGroup(
            Text("1. Selección por Torneo (k=3)", font_size=16, color=WHITE),
            Text("2. Cruzamiento Ordenado (OX)", font_size=16, color=WHITE),
            Text("3. Mutación por Intercambio (tasa=0.1)", font_size=16, color=WHITE),
            Text("4. Evaluación de Fitness", font_size=16, color=WHITE),
            Text("5. Reemplazo Generacional", font_size=16, color=WHITE)
        )
        
        operadores.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        operadores.to_edge(LEFT, buff=1).shift(UP * 0.5)
        
        self.play(Write(operadores), run_time=3)
        
        # Área de demostración visual
        demo_area = Rectangle(width=7, height=4.5, color=GRAY, fill_opacity=0.1, stroke_width=2)
        demo_area.to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)
        
        self.play(Create(demo_area))
        
        # DEMOSTRACIÓN 1: SELECCIÓN POR TORNEO
        self.play(operadores[0].animate.set_color(YELLOW))
        
        seleccion_titulo = Text("Selección por Torneo", font_size=16, weight=BOLD, color=YELLOW)
        seleccion_titulo.next_to(demo_area, UP, buff=0.2)
        
        self.play(Write(seleccion_titulo))
        
        # Mostrar población con fitness values (basado en su código seleccionar_padres)
        individuos_demo = VGroup()
        fitness_values = [45.2, 38.7, 52.1, 41.3, 36.9, 48.6]  # Valores en millones
        
        for i, fitness in enumerate(fitness_values):
            # Representación visual del individuo
            individuo_rect = Rectangle(width=0.8, height=0.4, color=BLUE, fill_opacity=0.6)
            fitness_text = Text(f"{fitness}M", font_size=10, color=WHITE)
            
            individuo_grupo = VGroup(individuo_rect, fitness_text)
            individuo_grupo.shift(RIGHT * (i - 2.5) * 1.0 + UP * 1.5)
            individuo_grupo.move_to(demo_area.get_center() + RIGHT * (i - 2.5) * 1.0 + UP * 1.2)
            
            individuos_demo.add(individuo_grupo)
        
        self.play(Create(individuos_demo), run_time=2)
        
        # Simular torneo (k=3 como en su código)
        seleccionados = random.sample(range(6), 3)
        
        for i in seleccionados:
            self.play(individuos_demo[i].animate.set_color(ORANGE), run_time=0.5)
        
        # Destacar ganador (menor fitness)
        fitness_seleccionados = [fitness_values[i] for i in seleccionados]
        ganador_idx = seleccionados[fitness_seleccionados.index(min(fitness_seleccionados))]
        
        self.play(individuos_demo[ganador_idx].animate.set_color(GREEN), run_time=1)
        self.wait(1)
        
        # Resetear colores
        for i in seleccionados:
            self.play(individuos_demo[i].animate.set_color(BLUE), run_time=0.2)
        
        self.play(operadores[0].animate.set_color(WHITE))
        
        # DEMOSTRACIÓN 2: CRUZAMIENTO ORDENADO (OX)
        self.play(operadores[1].animate.set_color(YELLOW))
        
        self.play(FadeOut(individuos_demo))
        
        cruce_titulo = Text("Cruzamiento Ordenado (OX)", font_size=16, weight=BOLD, color=YELLOW)
        cruce_titulo.next_to(demo_area, UP, buff=0.2)
        
        # Eliminar el título anterior y crear el nuevo
        self.play(FadeOut(seleccion_titulo))
        self.play(Write(cruce_titulo))
        
        # Mostrar dos padres (basado en su función cruce_ordenado)
        padre1_seq = [1, 2, 3, 4, 5, 6, 7, 8]
        padre2_seq = [3, 7, 5, 1, 6, 8, 2, 4]
        
        # Visualización de padres
        padre1_visual = VGroup()
        padre2_visual = VGroup()
        
        for i, (p1, p2) in enumerate(zip(padre1_seq, padre2_seq)):
            # Padre 1
            c1 = Circle(radius=0.15, color=BLUE, fill_opacity=0.8)
            t1 = Text(str(p1), font_size=10, color=WHITE)
            g1 = VGroup(c1, t1)
            g1.shift(RIGHT * (i - 3.5) * 0.4)
            padre1_visual.add(g1)
            
            # Padre 2
            c2 = Circle(radius=0.15, color=RED, fill_opacity=0.8)
            t2 = Text(str(p2), font_size=10, color=WHITE)
            g2 = VGroup(c2, t2)
            g2.shift(RIGHT * (i - 3.5) * 0.4)
            padre2_visual.add(g2)
        
        padre1_visual.move_to(demo_area.get_center() + UP * 1)
        padre2_visual.move_to(demo_area.get_center() + UP * 0.2)
        
        padre1_label = Text("Padre 1:", font_size=12, color=BLUE)
        padre2_label = Text("Padre 2:", font_size=12, color=RED)
        
        padre1_label.next_to(padre1_visual, LEFT, buff=0.3)
        padre2_label.next_to(padre2_visual, LEFT, buff=0.3)
        
        self.play(Create(VGroup(padre1_visual, padre2_visual, padre1_label, padre2_label)), run_time=2)
        
        # Seleccionar segmento de cruce (a=2, b=5 como en el algoritmo OX)
        inicio, fin = 2, 5
        segmento_highlight = Rectangle(width=1.8, height=0.4, color=YELLOW, 
                                     stroke_width=3, fill_opacity=0.2)
        segmento_highlight.move_to(padre1_visual[inicio:fin+1].get_center())
        
        self.play(Create(segmento_highlight))
        
        # Resaltar segmento copiado
        for i in range(inicio, fin+1):
            self.play(padre1_visual[i].animate.set_color(YELLOW), run_time=0.3)
        
        # Mostrar hijo resultante
        hijo_visual = VGroup()
        hijo_sequence = [None] * 8
        
        # Copiar segmento del padre 1
        for i in range(inicio, fin+1):
            hijo_sequence[i] = padre1_seq[i]
        
        # Crear visualización del hijo
        for i in range(8):
            if i >= inicio and i <= fin:
                c = Circle(radius=0.15, color=YELLOW, fill_opacity=0.8)
                t = Text(str(hijo_sequence[i]), font_size=10, color=BLACK)
            else:
                c = Circle(radius=0.15, color=GRAY, fill_opacity=0.3, stroke_width=2)
                t = Text("?", font_size=10, color=WHITE)
            
            g = VGroup(c, t)
            g.shift(RIGHT * (i - 3.5) * 0.4)
            hijo_visual.add(g)
        
        hijo_visual.move_to(demo_area.get_center() + DOWN * 0.6)
        hijo_label = Text("Hijo:", font_size=12, color=YELLOW)
        hijo_label.next_to(hijo_visual, LEFT, buff=0.3)
        
        self.play(Create(VGroup(hijo_visual, hijo_label)), run_time=1.5)
        
        # Completar hijo con elementos del padre 2 (algoritmo OX completo)
        elementos_restantes = [x for x in padre2_seq if x not in hijo_sequence[inicio:fin+1]]
        posiciones_vacias = [i for i in range(8) if i < inicio or i > fin]
        
        for j, pos in enumerate(posiciones_vacias):
            if j < len(elementos_restantes):
                elemento = elementos_restantes[j]
                c = Circle(radius=0.15, color=GREEN, fill_opacity=0.8)
                t = Text(str(elemento), font_size=10, color=WHITE)
                g = VGroup(c, t)
                g.move_to(hijo_visual[pos].get_center())
                
                self.play(Transform(hijo_visual[pos], g), run_time=0.6)
        
        self.wait(2)
        self.play(operadores[1].animate.set_color(WHITE))
        
        # DEMOSTRACIÓN 3: MUTACIÓN
        self.play(operadores[2].animate.set_color(YELLOW))
        
        # Limpiar elementos de la demostración anterior INCLUYENDO el título
        self.play(FadeOut(VGroup(padre1_visual, padre2_visual, padre1_label, 
                                padre2_label, segmento_highlight, cruce_titulo)))
        
        # Crear nuevo título para mutación en posición clara
        mutacion_titulo = Text("Mutación por Intercambio", font_size=16, weight=BOLD, color=YELLOW)
        mutacion_titulo.next_to(demo_area, UP, buff=0.2)
        
        self.play(Write(mutacion_titulo))
        
        # Fórmula de tasa de mutación (corregida para LaTeX)
        formula_mutacion = MathTex(r"\text{Tasa de mutacion} = 0.1", font_size=16, color=WHITE)
        formula_mutacion.move_to(demo_area.get_center() + UP * 1.5)
        
        self.play(Write(formula_mutacion))
        
        # Mostrar mutación en el hijo
        pos1, pos2 = 1, 5  # Posiciones a intercambiar
        
        # Resaltar posiciones
        self.play(hijo_visual[pos1].animate.set_color(RED),
                 hijo_visual[pos2].animate.set_color(RED), run_time=1)
        
        # Intercambio visual
        pos1_center = hijo_visual[pos1].get_center()
        pos2_center = hijo_visual[pos2].get_center()
        
        self.play(hijo_visual[pos1].animate.move_to(pos2_center),
                 hijo_visual[pos2].animate.move_to(pos1_center), run_time=1.5)
        
        self.wait(1)
        self.play(operadores[2].animate.set_color(WHITE))
        
        # SECCIÓN 3: MÉTRICAS DE EVALUACIÓN
        # Limpiar completamente la pantalla antes de la nueva sección
        self.play(FadeOut(VGroup(hijo_visual, hijo_label, formula_mutacion, mutacion_titulo)))
        
        # Crear título de métricas en posición clara
        metricas_titulo = Text("Métricas de Evaluación", font_size=16, weight=BOLD, color=PURPLE)
        metricas_titulo.next_to(demo_area, UP, buff=0.2)
        
        self.play(Write(metricas_titulo))
        
        # Cuadro I de su artículo: Métricas de Evaluación
        metricas_cuadro = VGroup(
            Text("Cuadro I: Métricas de Evaluación de Rendimiento", 
                font_size=14, weight=BOLD, color=ORANGE),
            Text("Métrica", font_size=12, weight=BOLD, color=YELLOW),
            Text("Calidad de Solución: f_mejor", font_size=11, color=WHITE),
            Text("Vel. de Convergencia: G95%", font_size=11, color=WHITE),
            Text("Tiempo Computacional: T_total", font_size=11, color=WHITE)
        )
        
        # Fórmulas específicas de su artículo (con notación compatible LaTeX)
        formula_exito = MathTex(r"TE = \frac{n_{exito}}{n_{total}} \times 100\%", 
                               font_size=14, color=WHITE)
        
        formula_diversidad = MathTex(r"ID = \frac{1}{n}\sum_{i=1}^{n} d(x_i, \bar{x})", 
                                   font_size=14, color=WHITE)
        
        metricas_completas = VGroup(
            metricas_cuadro[0],
            metricas_cuadro[1], metricas_cuadro[2], metricas_cuadro[3], metricas_cuadro[4],
            formula_exito,
            formula_diversidad
        )
        
        metricas_completas.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        metricas_completas.move_to(demo_area.get_center())
        
        self.play(Write(metricas_completas), run_time=4)
        self.wait(2)
        
        # SECCIÓN 4: CONVERGENCIA Y RESULTADOS
        self.play(FadeOut(VGroup(operadores, demo_area, metricas_completas, metricas_titulo)))
        
        resultados_titulo = Text("Convergencia del Algoritmo Genético", 
                                font_size=20, weight=BOLD, color=GREEN)
        resultados_titulo.to_edge(UP, buff=1)
        
        self.play(Transform(titulo, resultados_titulo))
        
        # Gráfico de convergencia (basado en sus datos reales)
        axes = Axes(
            x_range=[0, 100, 25],
            y_range=[35, 75, 10],
            x_length=8,
            y_length=4,
            axis_config={"color": GRAY, "stroke_width": 2},
            tips=False
        )
        axes.shift(DOWN * 0.5)
        
        # Etiquetas
        x_label = Text("Generación", font_size=12, color=WHITE)
        x_label.next_to(axes, DOWN, buff=0.3)
        
        y_label = Text("Distancia (Millones de metros)", font_size=12, color=WHITE)
        y_label.next_to(axes, LEFT, buff=0.3).rotate(PI/2)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # Curva de convergencia basada en sus resultados experimentales
        generaciones = np.linspace(0, 100, 100)
        # Convergencia de ~75M a ~35M metros según sus datos
        distancias = 75 * np.exp(-generaciones/30) + 35 + np.random.normal(0, 1, 100) * 0.5
        distancias = np.clip(distancias, 35, 75)
        
        puntos = [axes.coords_to_point(x, y) for x, y in zip(generaciones, distancias)]
        curva_convergencia = VMobject()
        curva_convergencia.set_points_smoothly(puntos)
        curva_convergencia.set_color(GREEN)
        curva_convergencia.set_stroke_width(3)
        
        self.play(Create(curva_convergencia), run_time=4)
        
        # Cuadro II: Parámetros Experimentales (de su artículo)
        parametros_cuadro = VGroup(
            Text("Cuadro II: Parámetros Experimentales", 
                font_size=14, weight=BOLD, color=BLUE),
            Text("Corridas por instancia: 30", font_size=12, color=WHITE),
            Text("Máx. generaciones: 1000", font_size=12, color=WHITE),
            Text("Tamaño población: 50-200 (adaptativo)", font_size=12, color=WHITE),
            Text("Significancia: α = 0.05", font_size=12, color=WHITE)
        )
        
        parametros_cuadro.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        parametros_cuadro.to_corner(UR, buff=0.5)
        
        self.play(Write(parametros_cuadro), run_time=3)
        
        # Resultados finales (sus datos exactos)
        resultados_finales = VGroup(
            Text("Resultados del Algoritmo Genético:", font_size=16, weight=BOLD, color=GREEN),
            Text("Distancia final: 34,892,902 metros", font_size=14, color=GREEN),
            Text("Mejora vs Aleatorio: 40.1%", font_size=14, color=YELLOW),
            Text("Convergencia: ~650 generaciones", font_size=14, color=BLUE),
            Text("Tasa de éxito: 53.3%", font_size=14, color=WHITE)
        )
        
        resultados_finales.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        resultados_finales.to_edge(DOWN, buff=0.8)
        
        self.play(Write(resultados_finales), run_time=3)
        self.wait(2)
        
        # Conclusión
        conclusion = Text("El Algoritmo Genético demuestra mejora significativa sobre búsqueda aleatoria", 
                         font_size=16, weight=BOLD, color=ORANGE)
        conclusion.to_edge(DOWN, buff=0.2)
        
        self.play(Transform(resultados_finales[-1], conclusion), run_time=2)
        self.wait(2)
        
        # Transición
        transicion = Text("Sin embargo, los algoritmos híbridos pueden superar estos resultados...", 
                         font_size=16, weight=BOLD, color=PURPLE)
        transicion.move_to(ORIGIN)
        
        self.play(FadeOut(VGroup(titulo, axes, x_label, y_label, curva_convergencia,
                                parametros_cuadro, resultados_finales)))
        
        self.play(Write(transicion), run_time=2)
        self.wait(2)
        
        self.play(FadeOut(transicion))
        self.wait(1)