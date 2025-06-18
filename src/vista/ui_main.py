"""
Archivo generado automáticamente por pyuic6.
Este archivo simula la salida de Qt Designer convertida a código Python.
"""

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    """Clase que define la interfaz de usuario de la ventana principal."""
    
    def setupUi(self, MainWindow):
        """
        Configura la interfaz de usuario de la ventana principal.
        
        Args:
            MainWindow: Instancia de QMainWindow donde se configurará la UI.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("Calculadora de Áreas - PyQt6")
        
        # Widget central
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Layout principal
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Etiqueta de bienvenida
        self.label_bienvenida = QtWidgets.QLabel(self.centralwidget)
        self.label_bienvenida.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_bienvenida.setObjectName("label_bienvenida")
        self.label_bienvenida.setText("Calculadora de Áreas de Figuras Geométricas")
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_bienvenida.setFont(font)
        self.verticalLayout.addWidget(self.label_bienvenida)
        
        # Espaciador
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, 
                                          QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        
        # Etiqueta de instrucciones
        self.label_instrucciones = QtWidgets.QLabel(self.centralwidget)
        self.label_instrucciones.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_instrucciones.setObjectName("label_instrucciones")
        self.label_instrucciones.setText("Selecciona una figura geométrica del menú 'Cálculo de Áreas'")
        self.verticalLayout.addWidget(self.label_instrucciones)
        
        # Espaciador
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, 
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Barra de menú
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        
        # Menú "Cálculo de Áreas"
        self.menuCalculo_Areas = QtWidgets.QMenu(self.menubar)
        self.menuCalculo_Areas.setObjectName("menuCalculo_Areas")
        self.menuCalculo_Areas.setTitle("Cálculo de Áreas")
        
        # Menú "Archivo"
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuArchivo.setTitle("Archivo")
        
        MainWindow.setMenuBar(self.menubar)
        
        # Barra de estado
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # Acciones del menú
        self.actionCirculo = QtGui.QAction(MainWindow)
        self.actionCirculo.setObjectName("actionCirculo")
        self.actionCirculo.setText("Círculo")
        
        self.actionTriangulo = QtGui.QAction(MainWindow)
        self.actionTriangulo.setObjectName("actionTriangulo")
        self.actionTriangulo.setText("Triángulo")
        
        self.actionRectangulo = QtGui.QAction(MainWindow)
        self.actionRectangulo.setObjectName("actionRectangulo")
        self.actionRectangulo.setText("Rectángulo")
        
        self.actionCuadrado = QtGui.QAction(MainWindow)
        self.actionCuadrado.setObjectName("actionCuadrado")
        self.actionCuadrado.setText("Cuadrado")
        
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionSalir.setText("Salir")
        self.actionSalir.setShortcut("Ctrl+Q")
        
        # Agregar acciones a los menús
        self.menuCalculo_Areas.addAction(self.actionCirculo)
        self.menuCalculo_Areas.addAction(self.actionTriangulo)
        self.menuCalculo_Areas.addAction(self.actionRectangulo)
        self.menuCalculo_Areas.addAction(self.actionCuadrado)
        self.menuCalculo_Areas.setShortcut("Ctrl+A")
        
        self.menuArchivo.addAction(self.actionSalir)
        
        self.menubar.addAction(self.menuCalculo_Areas.menuAction())
        self.menubar.addAction(self.menuArchivo.menuAction())
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
