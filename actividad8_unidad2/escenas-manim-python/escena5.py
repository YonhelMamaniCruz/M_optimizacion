from manim import *
import numpy as np

class AlgoritmoEvolutivoHibrido(Scene):
    def construct(self):
        # Título principal destacando la innovación
        titulo = Text("Algoritmo Evolutivo Hibrido", 
                     font_size=32, weight=BOLD, color=GOLD)
        titulo.to_edge(UP, buff=0.5)
        
        self.play(Write(titulo), run_time=2)
        
        # Subtítulo de contribución
        subtitulo = Text("Contribucion Principal de la Investigacion", 
                        font_size=18, color=ORANGE)
        subtitulo.next_to(titulo, DOWN, buff=0.3)
        
        self.play(Write(subtitulo), run_time=1.5)
        self.wait(1)
        
        # SECCIÓN 1: CONCEPTO DE HIBRIDACIÓN
        self.play(FadeOut(subtitulo))
        
        concepto_titulo = Text("Concepto de Hibridacion Evolutiva", 
                              font_size=20, weight=BOLD, color=PURPLE)
        concepto_titulo.to_edge(LEFT, buff=1).shift(UP * 2.5)
        
        self.play(Write(concepto_titulo))
        
        # Explicación conceptual con validación de contenido
        concepto_linea1 = Text("Integracion sinergica de multiples paradigmas evolutivos", 
                              font_size=16, color=WHITE)
        concepto_linea2 = Text("para maximizar eficiencia en espacios de alta dimensionalidad", 
                              font_size=16, color=WHITE)
        
        concepto_texto = VGroup(concepto_linea1, concepto_linea2)
        concepto_texto.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        concepto_texto.next_to(concepto_titulo, DOWN, buff=0.5)
        
        self.play(Write(concepto_texto), run_time=2.5)
        
        # Área de visualización principal con validación de dimensiones
        demo_area = Rectangle(width=8, height=4.5, color=GRAY, fill_opacity=0.1, stroke_width=2)
        demo_area.to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)
        
        self.play(Create(demo_area))
        
        # Componentes del algoritmo híbrido
        componentes_titulo = Text("Componentes Integrados", 
                                 font_size=16, weight=BOLD, color=YELLOW)
        componentes_titulo.next_to(demo_area, UP, buff=0.2)
        
        self.play(Write(componentes_titulo))
        
        # Lista de componentes con elementos individuales para mayor control
        comp1 = Text("1. Algoritmo Genetico Base", font_size=14, color=BLUE)
        comp2 = Text("2. Busqueda Local Intensiva", font_size=14, color=GREEN)
        comp3 = Text("3. Multi-poblacion con Migracion", font_size=14, color=ORANGE)
        comp4 = Text("4. Adaptacion Dinamica de Parametros", font_size=14, color=PURPLE)
        comp5 = Text("5. Operadores Especializados", font_size=14, color=YELLOW)
        
        componentes = VGroup(comp1, comp2, comp3, comp4, comp5)
        componentes.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        componentes.to_edge(LEFT, buff=1).shift(DOWN * 0.5)
        
        self.play(Write(componentes), run_time=3)
        self.wait(1)
        
        # DEMOSTRACIÓN 1: MULTI-POBLACIÓN (simplificada para estabilidad)
        self.play(comp3.animate.set_color(YELLOW))
        
        # Crear visualización de múltiples poblaciones con validación
        poblaciones = VGroup()
        n_poblaciones = 3
        colores_pob = [BLUE, RED, GREEN]
        nombres_pob = ["Poblacion A", "Poblacion B", "Poblacion C"]
        
        for i in range(n_poblaciones):
            # Validar índices y posiciones
            if i < len(colores_pob) and i < len(nombres_pob):
                poblacion_grupo = VGroup()
                
                # Título de población
                titulo_pob = Text(nombres_pob[i], font_size=10, color=colores_pob[i], weight=BOLD)
                titulo_pob.shift(UP * (1.5 - i * 1.2) + LEFT * 2)
                poblacion_grupo.add(titulo_pob)
                
                # Individuos de la población con validación de posiciones
                individuos = VGroup()
                for j in range(6):
                    individuo = Circle(radius=0.08, color=colores_pob[i], fill_opacity=0.8)
                    x_pos = j * 0.25 - 0.625
                    y_pos = 1.2 - i * 1.2
                    
                    # Validar que las posiciones estén en rango razonable
                    if abs(x_pos) < 5 and abs(y_pos) < 5:
                        individuo.shift(RIGHT * x_pos + UP * y_pos)
                        individuos.add(individuo)
                
                poblacion_grupo.add(individuos)
                poblaciones.add(poblacion_grupo)
        
        poblaciones.move_to(demo_area.get_center())
        
        self.play(Create(poblaciones), run_time=2)
        
        # Mostrar migración entre poblaciones de manera simplificada
        migracion_texto = Text("Migracion de mejores individuos", 
                              font_size=12, color=YELLOW)
        migracion_texto.move_to(demo_area.get_center() + DOWN * 1.8)
        
        self.play(Write(migracion_texto))
        
        # Animación de migración simplificada
        if len(poblaciones) >= n_poblaciones:
            for ciclo in range(2):
                # Resaltar individuos de manera segura
                if len(poblaciones[0]) > 1 and len(poblaciones[0][1]) > 0:
                    mejores = VGroup()
                    for i in range(min(len(poblaciones), n_poblaciones)):
                        if len(poblaciones[i]) > 1 and len(poblaciones[i][1]) > 0:
                            mejor = poblaciones[i][1][0].copy()
                            mejor.set_color(YELLOW)
                            mejores.add(mejor)
                    
                    if len(mejores) > 0:
                        elementos_originales = VGroup()
                        for i in range(min(len(poblaciones), len(mejores))):
                            if len(poblaciones[i]) > 1 and len(poblaciones[i][1]) > 0:
                                elementos_originales.add(poblaciones[i][1][0])
                        
                        if len(elementos_originales) > 0:
                            self.play(Transform(elementos_originales, mejores), run_time=1)
                
                self.wait(0.5)
        
        self.play(comp3.animate.set_color(ORANGE))
        
        # DEMOSTRACIÓN 2: BÚSQUEDA LOCAL (mejorada y robusta)
        self.play(comp2.animate.set_color(YELLOW))
        
        self.play(FadeOut(VGroup(poblaciones, migracion_texto)))
        
        busqueda_titulo = Text("Busqueda Local Intensiva", 
                              font_size=14, weight=BOLD, color=GREEN)
        busqueda_titulo.move_to(demo_area.get_center() + UP * 1.5)
        
        self.play(Write(busqueda_titulo))
        
        # Visualizar búsqueda local con validación robusta
        ruta_demo = VGroup()
        n_nodos = 8
        radio = 1.2
        
        # Crear nodos con validación de posiciones
        nodos_pos = []
        for i in range(n_nodos):
            angulo = 2 * PI * i / n_nodos
            x = radio * np.cos(angulo)
            y = radio * np.sin(angulo)
            
            # Validar que las coordenadas estén en rango aceptable
            if abs(x) < 10 and abs(y) < 10:
                nodos_pos.append([x, y, 0])
                
                nodo = Circle(radius=0.08, color=WHITE, fill_opacity=1)
                nodo.move_to([x, y, 0])
                ruta_demo.add(nodo)
        
        # Validar que tenemos suficientes nodos
        if len(nodos_pos) >= 6:
            # Ruta inicial subóptima (simplificada)
            ruta_inicial = list(range(min(len(nodos_pos), 6))) + [0]
            lineas_iniciales = VGroup()
            
            for i in range(len(ruta_inicial) - 1):
                if (ruta_inicial[i] < len(nodos_pos) and 
                    ruta_inicial[i+1] < len(nodos_pos)):
                    
                    inicio = nodos_pos[ruta_inicial[i]]
                    fin = nodos_pos[ruta_inicial[i+1]]
                    linea = Line(inicio, fin, color=RED, stroke_width=2)
                    lineas_iniciales.add(linea)
            
            ruta_completa = VGroup(ruta_demo, lineas_iniciales)
            ruta_completa.move_to(demo_area.get_center()).shift(DOWN * 0.3)
            
            self.play(Create(ruta_completa), run_time=2)
            
            # Mostrar optimización de manera simplificada
            opt_texto = Text("Optimizacion 2-opt aplicada", 
                            font_size=12, color=GREEN)
            opt_texto.next_to(ruta_completa, DOWN, buff=0.5)
            
            self.play(Write(opt_texto))
            
            # Mostrar mejora visual simple
            if len(lineas_iniciales) > 0:
                nuevas_lineas = VGroup()
                for linea in lineas_iniciales:
                    nueva_linea = linea.copy()
                    nueva_linea.set_color(GREEN)
                    nuevas_lineas.add(nueva_linea)
                
                self.play(Transform(lineas_iniciales, nuevas_lineas), run_time=2)
            
            self.wait(1)
        
        self.play(comp2.animate.set_color(GREEN))
        
        # DEMOSTRACIÓN 3: ADAPTACIÓN DINÁMICA (simplificada)
        self.play(comp4.animate.set_color(YELLOW))
        
        # Limpiar elementos previos de manera segura
        elementos_busqueda = VGroup()
        if 'ruta_completa' in locals():
            elementos_busqueda.add(ruta_completa)
        if 'busqueda_titulo' in locals():
            elementos_busqueda.add(busqueda_titulo)
        if 'opt_texto' in locals():
            elementos_busqueda.add(opt_texto)
        
        if len(elementos_busqueda) > 0:
            self.play(FadeOut(elementos_busqueda))
        
        adaptacion_titulo = Text("Adaptacion Dinamica de Parametros", 
                                font_size=14, weight=BOLD, color=PURPLE)
        adaptacion_titulo.move_to(demo_area.get_center() + UP * 1.5)
        
        self.play(Write(adaptacion_titulo))
        
        # Descripción textual en lugar de gráfico complejo
        adaptacion_descripcion = VGroup(
            Text("Los parametros se ajustan automaticamente:", font_size=12, color=WHITE),
            Text("- Tasa de mutacion decrece con el tiempo", font_size=11, color=RED),
            Text("- Presion selectiva aumenta gradualmente", font_size=11, color=BLUE),
            Text("- Equilibrio exploracion-explotacion", font_size=11, color=GREEN)
        )
        
        adaptacion_descripcion.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        adaptacion_descripcion.move_to(demo_area.get_center())
        
        self.play(Write(adaptacion_descripcion), run_time=3)
        self.wait(2)
        
        self.play(comp4.animate.set_color(PURPLE))
        
        # SECCIÓN 2: RESULTADOS SUPERIORES (simplificada)
        self.play(FadeOut(VGroup(adaptacion_titulo, adaptacion_descripcion)))
        
        superioridad_titulo = Text("Resultados Superiores del Enfoque Hibrido", 
                                  font_size=16, weight=BOLD, color=GOLD)
        superioridad_titulo.move_to(demo_area.get_center() + UP * 1.5)
        
        self.play(Write(superioridad_titulo))
        
        # Resultados en formato de lista simple
        resultado1 = Text("Busqueda Aleatoria: 73.6M (0.0%)", font_size=12, color=WHITE)
        resultado2 = Text("Algoritmo Genetico: 42.2M (42.6%)", font_size=12, color=WHITE)
        resultado3 = Text("Evolucion Diferencial: 38.7M (47.4%)", font_size=12, color=WHITE)
        resultado4 = Text("Enjambre Particulas: 41.9M (43.1%)", font_size=12, color=WHITE)
        resultado5 = Text("Hibrido (Propuesto): 34.9M (52.6%)", font_size=12, color=GREEN, weight=BOLD)
        
        resultados = VGroup(resultado1, resultado2, resultado3, resultado4, resultado5)
        resultados.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        resultados.move_to(demo_area.get_center())
        
        # Animar resultados de manera controlada
        for resultado in resultados:
            self.play(Write(resultado), run_time=0.8)
            self.wait(0.2)
        
        # Destacar resultado híbrido
        destaque_hibrido = SurroundingRectangle(resultado5, color=GOLD, stroke_width=3, buff=0.1)
        self.play(Create(destaque_hibrido))
        
        self.wait(2)
        
        # SECCIÓN 3: VENTAJAS COMPETITIVAS (con limpieza completa)
        elementos_demo = VGroup(componentes, demo_area, componentes_titulo,
                               superioridad_titulo, resultados, destaque_hibrido)
        
        # También eliminar elementos conceptuales que pueden persistir
        elementos_conceptuales = VGroup(concepto_titulo, concepto_texto)
        
        self.play(FadeOut(VGroup(elementos_demo, elementos_conceptuales)))
        
        ventajas_titulo = Text("Ventajas del Algoritmo Hibrido", 
                              font_size=20, weight=BOLD, color=GOLD)
        ventajas_titulo.to_edge(UP, buff=1)
        
        self.play(Transform(titulo, ventajas_titulo))
        
        # Lista simplificada de ventajas con elementos independientes
        ventaja1 = Text("Mayor precision en optimizacion", font_size=16, color=GREEN)
        ventaja2 = Text("Convergencia mas estable", font_size=16, color=GREEN)
        ventaja3 = Text("Adaptacion automatica", font_size=16, color=GREEN)
        ventaja4 = Text("Aplicable a gran escala", font_size=16, color=GREEN)
        
        ventajas_lista = VGroup(ventaja1, ventaja2, ventaja3, ventaja4)
        ventajas_lista.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        ventajas_lista.move_to(ORIGIN).shift(UP * 0.5)
        
        # Crear viñetas como elementos separados para mejor control
        vinetas = VGroup()
        
        # Animar ventajas con viñetas de manera controlada
        for i, ventaja in enumerate(ventajas_lista):
            vineta = Text("✓", font_size=18, color=YELLOW, weight=BOLD)
            vineta.next_to(ventaja, LEFT, buff=0.3)
            vinetas.add(vineta)
            
            self.play(Write(vineta), Write(ventaja), run_time=1.2)
            self.wait(0.3)
        
        self.wait(2)
        
        # SECCIÓN 4: CONCLUSIÓN FINAL (con eliminación explícita de viñetas)
        impacto_titulo = Text("Impacto en Aplicaciones Reales", 
                             font_size=18, weight=BOLD, color=BLUE)
        impacto_titulo.to_edge(DOWN, buff=2)
        
        self.play(Write(impacto_titulo))
        
        aplicacion1 = Text("Reduccion de costos operacionales", font_size=14, color=WHITE)
        aplicacion2 = Text("Optimizacion de redes logisticas", font_size=14, color=WHITE)
        aplicacion3 = Text("Mejora en sistemas de transporte", font_size=14, color=BLUE)
        
        aplicaciones = VGroup(aplicacion1, aplicacion2, aplicacion3)
        aplicaciones.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        aplicaciones.next_to(impacto_titulo, DOWN, buff=0.3)
        
        self.play(Write(aplicaciones), run_time=2.5)
        self.wait(2)
        
        # CONTRIBUCIÓN CIENTÍFICA FINAL (eliminar explícitamente ventajas y viñetas)
        elementos_ventajas = VGroup(ventajas_lista, vinetas)
        elementos_aplicaciones = VGroup(impacto_titulo, aplicaciones)
        
        self.play(FadeOut(VGroup(elementos_ventajas, elementos_aplicaciones)))
        
        contribucion_final = Text("Contribucion Cientifica Validada", 
                                 font_size=24, weight=BOLD, color=PURPLE)
        contribucion_final.move_to(ORIGIN).shift(UP * 1.5)
        
        self.play(Write(contribucion_final))
        
        # Resumen de contribución en líneas separadas para mayor control
        resumen1 = Text("Este Algoritmo Evolutivo Hibrido representa una contribucion", 
                       font_size=16, color=WHITE)
        resumen2 = Text("significativa al campo de optimizacion combinatoria,", 
                       font_size=16, color=WHITE)
        resumen3 = Text("demostrando mejoras cuantificables del 52.6% sobre", 
                       font_size=16, color=WHITE)
        resumen4 = Text("metodos aleatorios en problemas de alta dimensionalidad.", 
                       font_size=16, color=WHITE)
        
        resumen_contribucion = VGroup(resumen1, resumen2, resumen3, resumen4)
        resumen_contribucion.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        resumen_contribucion.move_to(ORIGIN).shift(DOWN * 0.5)
        
        self.play(Write(resumen_contribucion), run_time=4)
        self.wait(2)
        
        # Mensaje final
        mensaje_final = Text("El futuro de la optimizacion evolutiva", 
                            font_size=20, weight=BOLD, color=GOLD)
        mensaje_final.to_edge(DOWN, buff=1)
        
        self.play(Write(mensaje_final), run_time=2)
        self.wait(2)
        
        # Agradecimientos finales
        agradecimiento1 = Text("Gracias por su atencion", font_size=24, weight=BOLD, color=GOLD)
        agradecimiento2 = Text("Yonhel Mamani Cruz", font_size=18, color=WHITE)
        agradecimiento3 = Text("Universidad Nacional del Altiplano", font_size=16, color=GRAY)
        agradecimiento4 = Text("Facultad de Ingenieria Estadistica e Informatica", font_size=14, color=GRAY)
        
        agradecimientos = VGroup(agradecimiento1, agradecimiento2, agradecimiento3, agradecimiento4)
        agradecimientos.arrange(DOWN, buff=0.3)
        agradecimientos.move_to(ORIGIN)
        
        # Transición final controlada
        elementos_finales = VGroup(titulo, contribucion_final, resumen_contribucion, mensaje_final)
        
        self.play(FadeOut(elementos_finales))
        self.play(Write(agradecimientos), run_time=3)
        self.wait(3)
        
        self.play(FadeOut(agradecimientos))
        self.wait(1)