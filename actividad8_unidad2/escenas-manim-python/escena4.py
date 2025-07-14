from manim import *
import numpy as np

class ComparacionResultados(Scene):
    def construct(self):
        # Título principal
        titulo = Text("Análisis Comparativo de Algoritmos Evolutivos", 
                     font_size=28, weight=BOLD, color=PURPLE)
        titulo.to_edge(UP, buff=0.5)
        
        self.play(Write(titulo), run_time=2)
        
        # Subtítulo metodológico
        subtitulo = Text("Evaluación experimental basada en 30 ejecuciones independientes", 
                        font_size=16, color=GRAY)
        subtitulo.next_to(titulo, DOWN, buff=0.3)
        
        self.play(Write(subtitulo), run_time=1.5)
        self.wait(1)
        
        # SECCIÓN 1: RESULTADOS EXPERIMENTALES
        self.play(FadeOut(subtitulo))
        
        # Cuadro III: Resultados Comparativos (basado exactamente en su artículo)
        resultados_titulo = Text("Cuadro III: Resultados Comparativos de Rendimiento", 
                                font_size=18, weight=BOLD, color=ORANGE)
        resultados_titulo.to_edge(LEFT, buff=0.5).shift(UP * 2.5)
        
        self.play(Write(resultados_titulo))
        
        # Datos exactos de su artículo (validados para prevenir errores)
        algoritmos = ["Aleatorio", "AG", "ED", "OEP", "AEH"]
        medias = [73.59, 42.16, 38.72, 41.89, 34.89]  # En millones (validados)
        desv_est = [8.25, 3.89, 2.16, 4.23, 1.79]     # Validados
        mejores = [61.42, 37.25, 35.89, 36.79, 32.57]  # Validados
        exito = [0.0, 23.3, 33.3, 26.7, 53.3]         # Validados
        
        # Validar datos para prevenir errores de renderización
        assert len(algoritmos) == len(medias) == len(desv_est) == len(mejores) == len(exito)
        assert all(isinstance(x, (int, float)) for x in medias + desv_est + mejores + exito)
        
        # Crear tabla comparativa con validación robusta
        tabla_headers = VGroup()
        headers_texto = ["Algoritmo", "Media", "Desv. Est.", "Mejor", "Éxito (%)"]
        
        for i, header_text in enumerate(headers_texto):
            header = Text(header_text, font_size=12, weight=BOLD, color=YELLOW)
            header.shift(RIGHT * (i - 2) * 1.8 + UP * 1.5)
            tabla_headers.add(header)
        
        self.play(Write(tabla_headers), run_time=2)
        
        # Crear filas de datos con validación de parámetros
        filas_datos = VGroup()
        
        for j, (alg, media, desv, mejor, ex) in enumerate(zip(algoritmos, medias, desv_est, mejores, exito)):
            # Validar valores antes de crear texto
            if not all(isinstance(val, (int, float)) for val in [media, desv, mejor, ex]):
                continue
                
            # Crear elementos de texto con manejo seguro de parámetros
            if alg == "AEH":  # Destacar el algoritmo híbrido
                color_fila = GREEN
                algoritmo_text = Text(str(alg), font_size=11, color=color_fila, weight=BOLD)
                media_text = Text(f"{float(media):.1f}M", font_size=11, color=color_fila, weight=BOLD)
                desv_text = Text(f"{float(desv):.1f}M", font_size=11, color=color_fila, weight=BOLD)
                mejor_text = Text(f"{float(mejor):.1f}M", font_size=11, color=color_fila, weight=BOLD)
                exito_text = Text(f"{float(ex):.1f}", font_size=11, color=color_fila, weight=BOLD)
            else:
                color_fila = WHITE
                algoritmo_text = Text(str(alg), font_size=11, color=color_fila)
                media_text = Text(f"{float(media):.1f}M", font_size=11, color=color_fila)
                desv_text = Text(f"{float(desv):.1f}M", font_size=11, color=color_fila)
                mejor_text = Text(f"{float(mejor):.1f}M", font_size=11, color=color_fila)
                exito_text = Text(f"{float(ex):.1f}", font_size=11, color=color_fila)
            
            fila = VGroup(algoritmo_text, media_text, desv_text, mejor_text, exito_text)
            
            # Posicionar elementos con validación de coordenadas
            for i, elemento in enumerate(fila):
                x_pos = (i - 2) * 1.8
                y_pos = 1 - j * 0.3
                # Validar que las posiciones estén en rango razonable
                if abs(x_pos) < 10 and abs(y_pos) < 10:
                    elemento.shift(RIGHT * x_pos + UP * y_pos)
            
            filas_datos.add(fila)
        
        # Animar aparición de filas de manera controlada
        for fila in filas_datos:
            self.play(Write(fila), run_time=1)
            self.wait(0.2)
        
        # Destacar resultados del AEH con validación
        if len(filas_datos) > 0:
            destacar_aeh = SurroundingRectangle(filas_datos[-1], color=GOLD, stroke_width=3, buff=0.1)
            self.play(Create(destacar_aeh))
            
            mejor_resultado = Text("Mejor rendimiento en todas las metricas", 
                                  font_size=14, weight=BOLD, color=GOLD)
            mejor_resultado.next_to(destacar_aeh, DOWN, buff=0.3)
            
            self.play(Write(mejor_resultado))
            self.wait(2)
        
        # SECCIÓN 2: GRÁFICO COMPARATIVO DE BARRAS (mejorado y validado)
        elementos_tabla = VGroup(resultados_titulo, tabla_headers, filas_datos)
        if 'destacar_aeh' in locals():
            elementos_tabla.add(destacar_aeh)
        if 'mejor_resultado' in locals():
            elementos_tabla.add(mejor_resultado)
            
        self.play(FadeOut(elementos_tabla))
        
        grafico_titulo = Text("Comparacion Visual de Rendimiento", 
                             font_size=20, weight=BOLD, color=BLUE)
        grafico_titulo.to_edge(UP, buff=1)
        
        self.play(Transform(titulo, grafico_titulo))
        
        # Crear gráfico de barras con validación robusta
        # Validar rangos para ejes
        max_valor = max(medias)
        min_valor = min(medias)
        rango_y = max_valor * 1.1  # Agregar margen
        
        axes_barras = Axes(
            x_range=[0, len(algoritmos) + 1, 1],
            y_range=[0, rango_y, rango_y/4],
            x_length=8,
            y_length=4,
            axis_config={"color": GRAY, "stroke_width": 2}
        )
        axes_barras.shift(DOWN * 0.5)
        
        # Etiquetas de ejes
        y_label = Text("Distancia Total (Millones de metros)", font_size=12, color=WHITE)
        y_label.next_to(axes_barras, LEFT, buff=0.3).rotate(PI/2)
        
        self.play(Create(axes_barras), Write(y_label))
        
        # Crear barras con validación completa
        barras = VGroup()
        colores_barras = [RED, BLUE, ORANGE, GREEN, PURPLE]
        
        for i, (alg, media, color) in enumerate(zip(algoritmos, medias, colores_barras)):
            # Validar valores antes de crear geometría
            if not isinstance(media, (int, float)) or media <= 0:
                continue
                
            # Calcular altura con validación de rango
            altura_normalizada = min(media / rango_y, 0.9)  # Limitar altura máxima
            altura_pixels = altura_normalizada * 4  # Escalar a altura del gráfico
            
            if altura_pixels > 0:  # Validar altura positiva
                barra = Rectangle(
                    width=0.8,
                    height=altura_pixels,
                    color=color,
                    fill_opacity=0.7,
                    stroke_width=2
                )
                
                # Posicionar con validación de coordenadas
                x_coord = i + 1
                y_coord = altura_pixels / 2
                
                if 0 < x_coord <= len(algoritmos) and y_coord > 0:
                    try:
                        punto_posicion = axes_barras.coords_to_point(x_coord, y_coord)
                        barra.move_to(punto_posicion)
                    except:
                        # Fallback a posicionamiento manual si coords_to_point falla
                        barra.move_to(RIGHT * (x_coord - 3) * 1.5 + UP * (y_coord - 2))
                
                # Etiqueta del algoritmo
                etiqueta_alg = Text(str(alg), font_size=10, color=WHITE)
                etiqueta_alg.next_to(barra, DOWN, buff=0.2)
                
                # Valor de la barra
                valor_barra = Text(f"{float(media):.1f}M", font_size=10, color=color, weight=BOLD)
                valor_barra.next_to(barra, UP, buff=0.1)
                
                barra_completa = VGroup(barra, etiqueta_alg, valor_barra)
                barras.add(barra_completa)
        
        # Animar construcción de barras de manera segura
        if len(barras) > 0:
            for barra in barras:
                if len(barra) > 0:  # Verificar que la barra tenga elementos
                    self.play(GrowFromEdge(barra[0], DOWN), run_time=0.8)
                    if len(barra) > 1:
                        self.play(Write(VGroup(barra[1], barra[2])), run_time=0.5)
            
            # Destacar la barra del AEH
            if len(barras) >= len(algoritmos):
                barra_aeh_highlight = SurroundingRectangle(barras[-1][0], color=GOLD, 
                                                          stroke_width=4, buff=0.1)
                self.play(Create(barra_aeh_highlight))
                self.wait(1)
        
        # SECCIÓN 3: ANÁLISIS DE MEJORA PORCENTUAL (con validación matemática)
        mejora_titulo = Text("Analisis de Mejora del Algoritmo Evolutivo Hibrido", 
                            font_size=16, weight=BOLD, color=GOLD)
        mejora_titulo.to_edge(RIGHT, buff=0.5).shift(UP * 2)
        
        self.play(Write(mejora_titulo))
        
        # Cálculos de mejora con validación matemática
        try:
            if medias[0] > 0 and medias[4] > 0:  # Validar denominadores
                mejora_vs_aleatorio = ((medias[0] - medias[4]) / medias[0]) * 100
                mejor_clasico = min(medias[1:4])
                if mejor_clasico > 0:
                    mejora_vs_mejor_clasico = ((mejor_clasico - medias[4]) / mejor_clasico) * 100
                else:
                    mejora_vs_mejor_clasico = 0
            else:
                mejora_vs_aleatorio = 0
                mejora_vs_mejor_clasico = 0
        except (ZeroDivisionError, IndexError):
            mejora_vs_aleatorio = 0
            mejora_vs_mejor_clasico = 0
        
        mejoras_texto = VGroup(
            Text("Mejoras conseguidas:", font_size=14, weight=BOLD, color=ORANGE),
            Text(f"vs Busqueda Aleatoria: {mejora_vs_aleatorio:.1f}%", font_size=12, color=WHITE),
            Text(f"vs Mejor Clasico (ED): {mejora_vs_mejor_clasico:.1f}%", font_size=12, color=WHITE),
            Text("Menor desviacion estandar: +estabilidad", font_size=12, color=GREEN),
            Text("Mayor tasa de exito: 53.3%", font_size=12, color=GREEN)
        )
        
        mejoras_texto.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        mejoras_texto.next_to(mejora_titulo, DOWN, buff=0.5)
        
        self.play(Write(mejoras_texto), run_time=4)
        self.wait(2)
        
        # SECCIÓN 4: REPRESENTACIÓN DE LÍNEA HORIZONTAL (simplificada y robusta)
        elementos_grafico = VGroup(axes_barras, y_label, barras)
        if 'barra_aeh_highlight' in locals():
            elementos_grafico.add(barra_aeh_highlight)
            
        self.play(FadeOut(elementos_grafico))
        
        linea_titulo = Text("Reduccion de Distancia Total", 
                           font_size=18, weight=BOLD, color=BLUE)
        linea_titulo.move_to(ORIGIN).shift(UP * 2)
        
        self.play(Write(linea_titulo))
        
        # Línea horizontal de comparación con validación
        linea_comparacion = Line(LEFT * 4, RIGHT * 4, color=GRAY, stroke_width=3)
        linea_comparacion.shift(UP * 0.5)
        
        # Puntos de comparación
        punto_aleatorio = Dot(LEFT * 4, color=RED, radius=0.12)
        punto_aeh = Dot(RIGHT * 4, color=GREEN, radius=0.12)
        
        # Etiquetas con validación de datos
        try:
            aleatorio_valor = f"{float(medias[0]):.1f}M"
            aeh_valor = f"{float(medias[4]):.1f}M"
        except (IndexError, ValueError):
            aleatorio_valor = "N/A"
            aeh_valor = "N/A"
        
        etiqueta_aleatorio = VGroup(
            Text("Busqueda", font_size=12, color=RED),
            Text("Aleatoria", font_size=12, color=RED),
            Text(aleatorio_valor, font_size=10, color=RED, weight=BOLD)
        )
        etiqueta_aleatorio.arrange(DOWN, buff=0.05)
        etiqueta_aleatorio.next_to(punto_aleatorio, UP, buff=0.3)
        
        etiqueta_aeh = VGroup(
            Text("Algoritmo", font_size=12, color=GREEN),
            Text("Evolutivo", font_size=12, color=GREEN),
            Text(aeh_valor, font_size=10, color=GREEN, weight=BOLD)
        )
        etiqueta_aeh.arrange(DOWN, buff=0.05)
        etiqueta_aeh.next_to(punto_aeh, UP, buff=0.3)
        
        # Flecha de mejora
        flecha_mejora = Arrow(LEFT * 4, RIGHT * 4, color=YELLOW, 
                             stroke_width=4, max_tip_length_to_length_ratio=0.08)
        flecha_mejora.shift(UP * 0.5)
        
        # Texto de mejora con validación
        try:
            diferencia_absoluta = medias[0] - medias[4]
            diferencia_texto = f"{diferencia_absoluta:.1f}M metros"
            mejora_texto_final = f"{mejora_vs_aleatorio:.1f}%"
        except:
            diferencia_texto = "N/A"
            mejora_texto_final = "N/A"
        
        texto_mejora = VGroup(
            Text(f"Reduccion: {diferencia_texto}", font_size=14, weight=BOLD, color=YELLOW),
            Text(f"Mejora: {mejora_texto_final}", font_size=14, weight=BOLD, color=YELLOW)
        )
        texto_mejora.arrange(DOWN, buff=0.2)
        texto_mejora.next_to(flecha_mejora, DOWN, buff=0.5)
        
        # Secuencia de animación controlada
        self.play(Create(linea_comparacion))
        self.play(Create(punto_aleatorio), Write(etiqueta_aleatorio))
        self.play(Create(punto_aeh), Write(etiqueta_aeh))
        self.wait(1)
        
        self.play(Create(flecha_mejora), run_time=2)
        self.play(Write(texto_mejora), run_time=2)
        self.wait(2)
        
        # CONCLUSIÓN FINAL
        conclusion_titulo = Text("Conclusiones del Analisis Comparativo", 
                                font_size=16, weight=BOLD, color=PURPLE)
        conclusion_titulo.to_edge(DOWN, buff=1.5)
        
        conclusiones = VGroup(
            Text("El Algoritmo Evolutivo Hibrido supera a todos los metodos evaluados", 
                font_size=12, color=WHITE),
            Text("Demuestra mayor estabilidad (menor desviacion estandar)", 
                font_size=12, color=WHITE),
            Text("Logra la mejor tasa de exito experimental (53.3%)", 
                font_size=12, color=WHITE),
            Text("Proporciona beneficios operacionales para aplicaciones reales", 
                font_size=12, color=GREEN)
        )
        
        conclusiones.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        conclusiones.next_to(conclusion_titulo, DOWN, buff=0.3)
        
        self.play(Write(conclusion_titulo))
        self.play(Write(conclusiones), run_time=3)
        self.wait(2)
        
        # Mensaje de transición (corregido)
        transicion = Text("El Algoritmo Evolutivo Hibrido representa un avance significativo\nen optimizacion de rutas de alta dimensionalidad", 
                         font_size=16, weight=BOLD, color=GOLD)
        transicion.move_to(ORIGIN)
        
        # Fade out controlado de todos los elementos
        elementos_finales = VGroup(mejora_titulo, mejoras_texto, linea_titulo,
                                  linea_comparacion, punto_aleatorio, punto_aeh,
                                  etiqueta_aleatorio, etiqueta_aeh, flecha_mejora,
                                  texto_mejora, conclusion_titulo, conclusiones)
        
        self.play(FadeOut(elementos_finales))
        self.play(Write(transicion), run_time=2)
        self.wait(3)
        
        self.play(FadeOut(transicion))
        self.wait(1)