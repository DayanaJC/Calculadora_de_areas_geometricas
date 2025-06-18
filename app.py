"""
Punto de entrada principal de la aplicación de cálculo de áreas.
Aplicación interactiva con PyQt6 y POO.
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QStatusBar
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon

from src.vista.calculadora_widget import CalculadoraWidget


class MainWindow(QMainWindow):
    """Ventana principal de la aplicación."""
    
    def __init__(self):
        """Inicializa la ventana principal."""
        super().__init__()
        self.setupUI()
        self.crear_menu()
        self.crear_barra_estado()
    
    def setupUI(self):
        """Configura la interfaz de usuario."""
        self.setWindowTitle("Calculadora de Áreas - PyQt6 Interactiva")
        self.setGeometry(100, 100, 1000, 700)
        
        # Widget central
        self.calculadora = CalculadoraWidget()
        self.setCentralWidget(self.calculadora)
        
        # Aplicar estilo general
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
        """)
    
    def crear_menu(self):
        """Crea la barra de menú."""
        menubar = self.menuBar()
        
        # Menú Archivo
        menu_archivo = menubar.addMenu("Archivo")
        
        # Acción Salir
        accion_salir = QAction("Salir", self)
        accion_salir.setShortcut("Ctrl+Q")
        accion_salir.setStatusTip("Salir de la aplicación")
        accion_salir.triggered.connect(self.close)
        menu_archivo.addAction(accion_salir)
        
        # Menú Ayuda
        menu_ayuda = menubar.addMenu("Ayuda")
        
        # Acción Acerca de
        accion_acerca = QAction("Acerca de", self)
        accion_acerca.setStatusTip("Información sobre la aplicación")
        accion_acerca.triggered.connect(self.mostrar_acerca_de)
        menu_ayuda.addAction(accion_acerca)
    
    def crear_barra_estado(self):
        """Crea la barra de estado."""
        self.statusBar().showMessage("Listo - Ingrese valores para calcular áreas automáticamente")
    
    def mostrar_acerca_de(self):
        """Muestra información sobre la aplicación."""
        from PyQt6.QtWidgets import QMessageBox
        
        QMessageBox.about(self, "Acerca de", 
                         """
                         <h3>Calculadora de Áreas Interactiva</h3>
                         <p><b>Versión:</b> 1.0</p>
                         <p><b>Desarrollado con:</b> PyQt6 y Python</p>
                         <p><b>Características:</b></p>
                         <ul>
                         <li>Cálculo automático en tiempo real</li>
                         <li>4 figuras geométricas</li>
                         <li>Interfaz moderna e intuitiva</li>
                         <li>Historial de cálculos</li>
                         </ul>
                         <p><b>Figuras soportadas:</b> Círculo, Triángulo, Rectángulo, Cuadrado</p>
                         """)


def main():
    """Función principal que inicia la aplicación."""
    app = QApplication(sys.argv)
    app.setApplicationName("Calculadora de Áreas Interactiva")
    app.setApplicationVersion("1.0")
    
    # Crear y mostrar la ventana principal
    ventana = MainWindow()
    ventana.show()
    
    # Ejecutar el bucle de eventos
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
