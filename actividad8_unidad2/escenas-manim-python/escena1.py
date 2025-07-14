from manim import *
import numpy as np

class IntroduccionProblema(Scene):
    def construct(self):
        # Título principal
        titulo = Text("Algoritmos Evolutivos para Optimización de Rutas", 
                     font_size=36, weight=BOLD, color=BLUE)
        subtitulo = Text("Espacios de Alta Dimensionalidad", 
                        font_size=24, color=GRAY)
        
        # Posicionar textos
        titulo.to_edge(UP, buff=0.5)
        subtitulo.next_to(titulo, DOWN, buff=0.3)
        
        # Animación de entrada
        self.play(Write(titulo), run_time=2)
        self.play(Write(subtitulo), run_time=1.5)
        self.wait(1)
        
        # Transición a la explicación del problema
        self.play(FadeOut(titulo), FadeOut(subtitulo))
        
        # Problema del Viajante de Comercio - Visualización
        problema_texto = Text("Problema de Ruteo de Vehículos", 
                             font_size=28, weight=BOLD, color=ORANGE)
        problema_texto.to_edge(UP, buff=1)
        
        self.play(Write(problema_texto), run_time=1.5)
        
        # Crear nodos de ciudades
        ciudades = VGroup()
        n_ciudades = 8
        radio = 2.5
        
        for i in range(n_ciudades):
            angulo = 2 * PI * i / n_ciudades
            x = radio * np.cos(angulo)
            y = radio * np.sin(angulo)
            
            ciudad = Circle(radius=0.15, color=BLUE, fill_opacity=1)
            ciudad.move_to([x, y, 0])
            
            # Etiqueta de ciudad
            etiqueta = Text(f"C{i+1}", font_size=14, color=WHITE)
            etiqueta.move_to(ciudad.get_center())
            
            ciudades.add(VGroup(ciudad, etiqueta))
        
        # Posicionar el grupo de ciudades
        ciudades.shift(DOWN * 0.5)
        
        # Animación de aparición de ciudades
        self.play(LaggedStart(*[Create(ciudad) for ciudad in ciudades], 
                             lag_ratio=0.2), run_time=2)
        
        # Mostrar algunas rutas posibles
        rutas_ejemplos = [
            [0, 1, 2, 3, 4, 5, 6, 7, 0],  # Ruta ordenada
            [0, 3, 1, 6, 2, 7, 4, 5, 0],  # Ruta aleatoria 1
            [0, 2, 5, 1, 7, 3, 6, 4, 0],  # Ruta aleatoria 2
        ]
        
        colores_rutas = [GREEN, RED, YELLOW]
        
        explicacion = Text("Múltiples rutas posibles:", font_size=20, color=WHITE)
        explicacion.to_edge(LEFT, buff=1).shift(UP * 1.5)
        self.play(Write(explicacion))
        
        lineas_ruta = VGroup()
        
        for i, (ruta, color) in enumerate(zip(rutas_ejemplos, colores_rutas)):
            nuevas_lineas = VGroup()
            
            for j in range(len(ruta) - 1):
                inicio = ciudades[ruta[j]][0].get_center()
                fin = ciudades[ruta[j+1]][0].get_center()
                linea = Line(inicio, fin, color=color, stroke_width=3)
                nuevas_lineas.add(linea)
            
            if i == 0:
                lineas_ruta = nuevas_lineas
                self.play(Create(lineas_ruta), run_time=2)
                self.wait(1)
            else:
                self.play(Transform(lineas_ruta, nuevas_lineas), run_time=1.5)
                self.wait(0.5)
        
        # Texto explicativo sobre complejidad
        complejidad_texto = VGroup(
            Text("Complejidad del problema:", font_size=20, weight=BOLD, color=ORANGE),
            Text("• 8 ciudades: 40,320 rutas posibles", font_size=16, color=WHITE),
            Text("• 62 ciudades: ~10^81 rutas posibles", font_size=16, color=WHITE),
            Text("• Búsqueda exhaustiva es imposible", font_size=16, color=RED)
        )
        
        complejidad_texto.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        complejidad_texto.to_edge(RIGHT, buff=1).shift(UP * 1)
        
        self.play(Write(complejidad_texto), run_time=3)
        self.wait(2)
        
        # Transición al espacio de búsqueda
        self.play(FadeOut(VGroup(problema_texto, ciudades, lineas_ruta, 
                                explicacion, complejidad_texto)))
        
        # Visualización simplificada del espacio de búsqueda (2D)
        espacio_titulo = Text("Espacio de Búsqueda de Alta Dimensionalidad", 
                             font_size=24, weight=BOLD, color=PURPLE)
        espacio_titulo.to_edge(UP, buff=1)
        
        self.play(Write(espacio_titulo))
        
        # Crear una representación 2D del paisaje de optimización
        # Usar contornos y gradientes para simular un paisaje 3D
        
        # Crear fondo con gradiente
        fondo = Rectangle(width=10, height=6, color=DARK_BLUE, fill_opacity=0.8)
        fondo.move_to(ORIGIN)
        
        self.play(Create(fondo))
        
        # Crear "montañas" como círculos concéntricos para representar el paisaje
        paisaje = VGroup()
        
        # Múltiples "valles" y "picos" en el espacio de optimización
        centros = [
            [-2, 1, 0], [2, -1, 0], [0, 1.5, 0], [-1.5, -1.5, 0], [1.5, 0.5, 0]
        ]
        
        # Usar colores estándar que están garantizados en todas las versiones
        colores_paisaje = [RED, ORANGE, YELLOW, GREEN, BLUE]
        
        for i, (centro, color_base) in enumerate(zip(centros, colores_paisaje)):
            # Crear círculos concéntricos para simular contornos topográficos
            for radio in [0.3, 0.6, 0.9]:
                circulo = Circle(radius=radio, color=color_base, 
                               fill_opacity=0.3 - radio*0.1, stroke_width=1)
                circulo.move_to(centro)
                paisaje.add(circulo)
        
        self.play(Create(paisaje), run_time=3)
        
        # Agregar puntos que representen soluciones
        puntos_solucion = VGroup()
        
        for _ in range(8):
            x = np.random.uniform(-4, 4)
            y = np.random.uniform(-2.5, 2.5)
            
            punto = Dot(point=[x, y, 0], radius=0.08, color=YELLOW)
            puntos_solucion.add(punto)
        
        self.play(Create(puntos_solucion), run_time=2)
        
        # Texto explicativo
        explicacion_paisaje = VGroup(
            Text("Cada punto representa una ruta posible", font_size=16, color=WHITE),
            Text("Colores indican calidad (azul=mejor, rojo=peor)", font_size=16, color=WHITE),
            Text("Objetivo: Encontrar las regiones azules", font_size=16, color=BLUE)
        )
        
        explicacion_paisaje.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explicacion_paisaje.to_corner(DR, buff=0.5)
        
        self.play(Write(explicacion_paisaje), run_time=3)
        self.wait(2)
        
        # Mostrar la "maldición de la dimensionalidad"
        maldicion_texto = Text("La 'Maldición de la Dimensionalidad'", 
                              font_size=20, weight=BOLD, color=RED)
        maldicion_texto.to_edge(LEFT, buff=1).shift(UP * 2)
        
        self.play(Write(maldicion_texto))
        
        # Animación que muestra cómo crece exponencialmente
        dimensiones = VGroup(
            Text("2D: 100 puntos", font_size=14, color=WHITE),
            Text("3D: 1,000 puntos", font_size=14, color=ORANGE),
            Text("4D: 10,000 puntos", font_size=14, color=RED),
            Text("62D: 10^81 puntos!", font_size=14, weight=BOLD, color=RED)
        )
        
        dimensiones.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        dimensiones.next_to(maldicion_texto, DOWN, buff=0.3)
        
        for dim in dimensiones:
            self.play(Write(dim), run_time=1)
            self.wait(0.5)
        
        self.wait(2)
        
        # Conclusión de la escena
        conclusion = Text("Se requieren algoritmos inteligentes para explorar eficientemente", 
                         font_size=18, weight=BOLD, color=GOLD)
        conclusion.to_edge(DOWN, buff=0.5)
        
        self.play(Write(conclusion), run_time=2)
        self.wait(2)
        
        # Transición final
        transicion = Text("Los Algoritmos Evolutivos ofrecen una solución poderosa", 
                         font_size=20, weight=BOLD, color=GREEN)
        transicion.move_to(ORIGIN)
        
        # Fade out todo excepto la transición
        self.play(FadeOut(VGroup(espacio_titulo, fondo, paisaje, puntos_solucion, 
                                explicacion_paisaje, maldicion_texto, dimensiones, conclusion)))
        
        self.play(Write(transicion), run_time=2)
        self.wait(2)
        
        self.play(FadeOut(transicion))
        self.wait(1)