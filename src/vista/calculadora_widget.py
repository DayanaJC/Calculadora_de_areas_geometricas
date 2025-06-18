"""
Widget principal de la calculadora de áreas.
Contiene la interfaz interactiva para todas las figuras geométricas.
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                            QLabel, QLineEdit, QPushButton, QTextEdit, 
                            QGroupBox, QFrame, QScrollArea)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont, QPalette

from src.logica.areas import Circulo, Triangulo, Rectangulo, Cuadrado


class CalculadoraWidget(QWidget):
    """Widget principal que contiene todas las calculadoras de figuras."""
    
    def __init__(self):
        """Inicializa el widget de la calculadora."""
        super().__init__()
        self.setupUI()
        self.conectar_eventos()
    
    def setupUI(self):
        """Configura la interfaz de usuario."""
        # Layout principal
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # Título principal
        titulo = QLabel("🧮 Calculadora de Áreas Interactiva")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #2c3e50;
                margin: 20px;
                padding: 10px;
                background-color: #ecf0f1;
                border-radius: 10px;
            }
        """)
        main_layout.addWidget(titulo)
        
        # Área de scroll para las calculadoras
        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QGridLayout(scroll_widget)
        
        # Crear las 4 calculadoras
        self.calc_circulo = self.crear_calculadora_circulo()
        self.calc_triangulo = self.crear_calculadora_triangulo()
        self.calc_rectangulo = self.crear_calculadora_rectangulo()
        self.calc_cuadrado = self.crear_calculadora_cuadrado()
        
        # Organizar en grid 2x2
        scroll_layout.addWidget(self.calc_circulo, 0, 0)
        scroll_layout.addWidget(self.calc_triangulo, 0, 1)
        scroll_layout.addWidget(self.calc_rectangulo, 1, 0)
        scroll_layout.addWidget(self.calc_cuadrado, 1, 1)
        
        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)
        
        # Área de resultados
        self.resultado_area = QTextEdit()
        self.resultado_area.setMaximumHeight(150)
        self.resultado_area.setPlaceholderText("Los resultados aparecerán aquí...")
        self.resultado_area.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 2px solid #dee2e6;
                border-radius: 8px;
                padding: 10px;
                font-family: 'Courier New', monospace;
                font-size: 12px;
            }
        """)
        main_layout.addWidget(QLabel("📊 Historial de Cálculos:"))
        main_layout.addWidget(self.resultado_area)
        
        # Botón para limpiar historial
        btn_limpiar = QPushButton("🗑️ Limpiar Historial")
        btn_limpiar.clicked.connect(self.limpiar_historial)
        btn_limpiar.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        main_layout.addWidget(btn_limpiar)
    
    def crear_calculadora_circulo(self):
        """Crea la calculadora para círculos."""
        group = QGroupBox("🔵 Círculo")
        layout = QVBoxLayout()
        
        # Campo de entrada
        self.radio_input = QLineEdit()
        self.radio_input.setPlaceholderText("Ingrese el radio")
        self.radio_input.returnPressed.connect(self.calcular_circulo)
        
        # Botón calcular
        btn_calcular = QPushButton("Calcular Área")
        btn_calcular.clicked.connect(self.calcular_circulo)
        
        # Resultado
        self.resultado_circulo = QLabel("Área: --")
        self.resultado_circulo.setStyleSheet("font-weight: bold; color: #27ae60;")
        
        # Agregar al layout
        layout.addWidget(QLabel("Radio:"))
        layout.addWidget(self.radio_input)
        layout.addWidget(btn_calcular)
        layout.addWidget(self.resultado_circulo)
        layout.addWidget(QLabel("Fórmula: π × r²"))
        
        self.aplicar_estilo_grupo(group, btn_calcular, "#3498db")
        group.setLayout(layout)
        return group
    
    def crear_calculadora_triangulo(self):
        """Crea la calculadora para triángulos."""
        group = QGroupBox("🔺 Triángulo")
        layout = QVBoxLayout()
        
        # Campos de entrada
        self.base_input = QLineEdit()
        self.base_input.setPlaceholderText("Ingrese la base")
        self.base_input.returnPressed.connect(self.calcular_triangulo)
        
        self.altura_input = QLineEdit()
        self.altura_input.setPlaceholderText("Ingrese la altura")
        self.altura_input.returnPressed.connect(self.calcular_triangulo)
        
        # Botón calcular
        btn_calcular = QPushButton("Calcular Área")
        btn_calcular.clicked.connect(self.calcular_triangulo)
        
        # Resultado
        self.resultado_triangulo = QLabel("Área: --")
        self.resultado_triangulo.setStyleSheet("font-weight: bold; color: #27ae60;")
        
        # Agregar al layout
        layout.addWidget(QLabel("Base:"))
        layout.addWidget(self.base_input)
        layout.addWidget(QLabel("Altura:"))
        layout.addWidget(self.altura_input)
        layout.addWidget(btn_calcular)
        layout.addWidget(self.resultado_triangulo)
        layout.addWidget(QLabel("Fórmula: (base × altura) ÷ 2"))
        
        self.aplicar_estilo_grupo(group, btn_calcular, "#e74c3c")
        group.setLayout(layout)
        return group
    
    def crear_calculadora_rectangulo(self):
        """Crea la calculadora para rectángulos."""
        group = QGroupBox("▭ Rectángulo")
        layout = QVBoxLayout()
        
        # Campos de entrada
        self.largo_input = QLineEdit()
        self.largo_input.setPlaceholderText("Ingrese el largo")
        self.largo_input.returnPressed.connect(self.calcular_rectangulo)
        
        self.ancho_input = QLineEdit()
        self.ancho_input.setPlaceholderText("Ingrese el ancho")
        self.ancho_input.returnPressed.connect(self.calcular_rectangulo)
        
        # Botón calcular
        btn_calcular = QPushButton("Calcular Área")
        btn_calcular.clicked.connect(self.calcular_rectangulo)
        
        # Resultado
        self.resultado_rectangulo = QLabel("Área: --")
        self.resultado_rectangulo.setStyleSheet("font-weight: bold; color: #27ae60;")
        
        # Agregar al layout
        layout.addWidget(QLabel("Largo:"))
        layout.addWidget(self.largo_input)
        layout.addWidget(QLabel("Ancho:"))
        layout.addWidget(self.ancho_input)
        layout.addWidget(btn_calcular)
        layout.addWidget(self.resultado_rectangulo)
        layout.addWidget(QLabel("Fórmula: largo × ancho"))
        
        self.aplicar_estilo_grupo(group, btn_calcular, "#f39c12")
        group.setLayout(layout)
        return group
    
    def crear_calculadora_cuadrado(self):
        """Crea la calculadora para cuadrados."""
        group = QGroupBox("⬜ Cuadrado")
        layout = QVBoxLayout()
        
        # Campo de entrada
        self.lado_input = QLineEdit()
        self.lado_input.setPlaceholderText("Ingrese el lado")
        self.lado_input.returnPressed.connect(self.calcular_cuadrado)
        
        # Botón calcular
        btn_calcular = QPushButton("Calcular Área")
        btn_calcular.clicked.connect(self.calcular_cuadrado)
        
        # Resultado
        self.resultado_cuadrado = QLabel("Área: --")
        self.resultado_cuadrado.setStyleSheet("font-weight: bold; color: #27ae60;")
        
        # Agregar al layout
        layout.addWidget(QLabel("Lado:"))
        layout.addWidget(self.lado_input)
        layout.addWidget(btn_calcular)
        layout.addWidget(self.resultado_cuadrado)
        layout.addWidget(QLabel("Fórmula: lado²"))
        
        self.aplicar_estilo_grupo(group, btn_calcular, "#9b59b6")
        group.setLayout(layout)
        return group
    
    def aplicar_estilo_grupo(self, group, boton, color):
        """Aplica estilos consistentes a los grupos."""
        group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                border: 2px solid {color};
                border-radius: 10px;
                margin-top: 10px;
                padding-top: 10px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: {color};
            }}
            QLineEdit {{
                padding: 8px;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                font-size: 14px;
            }}
            QLineEdit:focus {{
                border-color: {color};
            }}
        """)
        
        boton.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 14px;
            }}
            QPushButton:hover {{
                background-color: {self.oscurecer_color(color)};
            }}
            QPushButton:pressed {{
                background-color: {self.oscurecer_color(color, 0.3)};
            }}
        """)
    
    def oscurecer_color(self, color, factor=0.2):
        """Oscurece un color hexadecimal."""
        color = color.lstrip('#')
        rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        rgb_oscuro = tuple(int(c * (1 - factor)) for c in rgb)
        return f"#{rgb_oscuro[0]:02x}{rgb_oscuro[1]:02x}{rgb_oscuro[2]:02x}"
    
    def conectar_eventos(self):
        """Conecta los eventos de entrada de texto."""
        # Conectar eventos de cambio de texto para cálculo automático
        self.radio_input.textChanged.connect(self.calcular_circulo_auto)
        self.base_input.textChanged.connect(self.calcular_triangulo_auto)
        self.altura_input.textChanged.connect(self.calcular_triangulo_auto)
        self.largo_input.textChanged.connect(self.calcular_rectangulo_auto)
        self.ancho_input.textChanged.connect(self.calcular_rectangulo_auto)
        self.lado_input.textChanged.connect(self.calcular_cuadrado_auto)
    
    def calcular_circulo(self):
        """Calcula el área del círculo."""
        try:
            radio = float(self.radio_input.text())
            circulo = Circulo(radio)
            area = circulo.calcular_area()
            
            self.resultado_circulo.setText(f"Área: {area:.4f} u²")
            self.agregar_al_historial(f"🔵 Círculo (r={radio}): {area:.4f} u²")
            
        except ValueError as e:
            if self.radio_input.text().strip():
                self.resultado_circulo.setText("Error: Valor inválido")
            else:
                self.resultado_circulo.setText("Área: --")
        except Exception as e:
            self.resultado_circulo.setText(f"Error: {str(e)}")
    
    def calcular_circulo_auto(self):
        """Calcula automáticamente cuando cambia el texto."""
        if self.radio_input.text().strip():
            self.calcular_circulo()
    
    def calcular_triangulo(self):
        """Calcula el área del triángulo."""
        try:
            base = float(self.base_input.text())
            altura = float(self.altura_input.text())
            triangulo = Triangulo(base, altura)
            area = triangulo.calcular_area()
            
            self.resultado_triangulo.setText(f"Área: {area:.4f} u²")
            self.agregar_al_historial(f"🔺 Triángulo (b={base}, h={altura}): {area:.4f} u²")
            
        except ValueError as e:
            if self.base_input.text().strip() and self.altura_input.text().strip():
                self.resultado_triangulo.setText("Error: Valores inválidos")
            else:
                self.resultado_triangulo.setText("Área: --")
        except Exception as e:
            self.resultado_triangulo.setText(f"Error: {str(e)}")
    
    def calcular_triangulo_auto(self):
        """Calcula automáticamente cuando cambian los textos."""
        if self.base_input.text().strip() and self.altura_input.text().strip():
            self.calcular_triangulo()
    
    def calcular_rectangulo(self):
        """Calcula el área del rectángulo."""
        try:
            largo = float(self.largo_input.text())
            ancho = float(self.ancho_input.text())
            rectangulo = Rectangulo(largo, ancho)
            area = rectangulo.calcular_area()
            
            self.resultado_rectangulo.setText(f"Área: {area:.4f} u²")
            self.agregar_al_historial(f"▭ Rectángulo (l={largo}, a={ancho}): {area:.4f} u²")
            
        except ValueError as e:
            if self.largo_input.text().strip() and self.ancho_input.text().strip():
                self.resultado_rectangulo.setText("Error: Valores inválidos")
            else:
                self.resultado_rectangulo.setText("Área: --")
        except Exception as e:
            self.resultado_rectangulo.setText(f"Error: {str(e)}")
    
    def calcular_rectangulo_auto(self):
        """Calcula automáticamente cuando cambian los textos."""
        if self.largo_input.text().strip() and self.ancho_input.text().strip():
            self.calcular_rectangulo()
    
    def calcular_cuadrado(self):
        """Calcula el área del cuadrado."""
        try:
            lado = float(self.lado_input.text())
            cuadrado = Cuadrado(lado)
            area = cuadrado.calcular_area()
            
            self.resultado_cuadrado.setText(f"Área: {area:.4f} u²")
            self.agregar_al_historial(f"⬜ Cuadrado (l={lado}): {area:.4f} u²")
            
        except ValueError as e:
            if self.lado_input.text().strip():
                self.resultado_cuadrado.setText("Error: Valor inválido")
            else:
                self.resultado_cuadrado.setText("Área: --")
        except Exception as e:
            self.resultado_cuadrado.setText(f"Error: {str(e)}")
    
    def calcular_cuadrado_auto(self):
        """Calcula automáticamente cuando cambia el texto."""
        if self.lado_input.text().strip():
            self.calcular_cuadrado()
    
    def agregar_al_historial(self, texto):
        """Agrega un resultado al historial."""
        self.resultado_area.append(texto)
        # Hacer scroll hacia abajo
        scrollbar = self.resultado_area.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def limpiar_historial(self):
        """Limpia el historial de resultados."""
        self.resultado_area.clear()
