"""
Versión simplificada para probar PyQt6
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QMessageBox

class VentanaSimple(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test PyQt6 - Calculadora de Áreas")
        self.setGeometry(300, 300, 400, 300)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Elementos
        titulo = QLabel("🧮 Calculadora de Áreas")
        titulo.setStyleSheet("font-size: 18px; font-weight: bold; margin: 20px;")
        
        btn_circulo = QPushButton("Calcular Área de Círculo")
        btn_circulo.clicked.connect(self.calcular_circulo)
        
        btn_cuadrado = QPushButton("Calcular Área de Cuadrado")
        btn_cuadrado.clicked.connect(self.calcular_cuadrado)
        
        # Agregar al layout
        layout.addWidget(titulo)
        layout.addWidget(btn_circulo)
        layout.addWidget(btn_cuadrado)
    
    def calcular_circulo(self):
        # Simulación simple
        import math
        radio = 5.0  # Valor fijo para prueba
        area = math.pi * radio ** 2
        QMessageBox.information(self, "Resultado", f"Área del círculo (radio={radio}): {area:.2f}")
    
    def calcular_cuadrado(self):
        # Simulación simple
        lado = 4.0  # Valor fijo para prueba
        area = lado ** 2
        QMessageBox.information(self, "Resultado", f"Área del cuadrado (lado={lado}): {area:.2f}")

def main():
    app = QApplication(sys.argv)
    ventana = VentanaSimple()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
