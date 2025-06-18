"""
Módulo para el cálculo de áreas de figuras geométricas.
Implementa clases usando Programación Orientada a Objetos.
"""

import math


class Circulo:
    """Clase para representar un círculo y calcular su área."""
    
    def __init__(self, radio: float):
        """
        Inicializa un círculo con el radio especificado.
        
        Args:
            radio (float): Radio del círculo. Debe ser positivo.
            
        Raises:
            ValueError: Si el radio es negativo o cero.
        """
        if radio <= 0:
            raise ValueError("El radio debe ser un número positivo")
        self.radio = radio
    
    def calcular_area(self) -> float:
        """
        Calcula el área del círculo usando la fórmula π * r².
        
        Returns:
            float: Área del círculo.
        """
        return math.pi * self.radio ** 2
    
    def __str__(self) -> str:
        """Representación en cadena del círculo."""
        return f"Círculo(radio={self.radio})"


class Triangulo:
    """Clase para representar un triángulo y calcular su área."""
    
    def __init__(self, base: float, altura: float):
        """
        Inicializa un triángulo con base y altura especificadas.
        
        Args:
            base (float): Base del triángulo. Debe ser positiva.
            altura (float): Altura del triángulo. Debe ser positiva.
            
        Raises:
            ValueError: Si la base o altura son negativas o cero.
        """
        if base <= 0:
            raise ValueError("La base debe ser un número positivo")
        if altura <= 0:
            raise ValueError("La altura debe ser un número positivo")
        self.base = base
        self.altura = altura
    
    def calcular_area(self) -> float:
        """
        Calcula el área del triángulo usando la fórmula (base * altura) / 2.
        
        Returns:
            float: Área del triángulo.
        """
        return (self.base * self.altura) / 2
    
    def __str__(self) -> str:
        """Representación en cadena del triángulo."""
        return f"Triángulo(base={self.base}, altura={self.altura})"


class Rectangulo:
    """Clase para representar un rectángulo y calcular su área."""
    
    def __init__(self, largo: float, ancho: float):
        """
        Inicializa un rectángulo con largo y ancho especificados.
        
        Args:
            largo (float): Largo del rectángulo. Debe ser positivo.
            ancho (float): Ancho del rectángulo. Debe ser positivo.
            
        Raises:
            ValueError: Si el largo o ancho son negativos o cero.
        """
        if largo <= 0:
            raise ValueError("El largo debe ser un número positivo")
        if ancho <= 0:
            raise ValueError("El ancho debe ser un número positivo")
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self) -> float:
        """
        Calcula el área del rectángulo usando la fórmula largo * ancho.
        
        Returns:
            float: Área del rectángulo.
        """
        return self.largo * self.ancho
    
    def __str__(self) -> str:
        """Representación en cadena del rectángulo."""
        return f"Rectángulo(largo={self.largo}, ancho={self.ancho})"


class Cuadrado:
    """Clase para representar un cuadrado y calcular su área."""
    
    def __init__(self, lado: float):
        """
        Inicializa un cuadrado con el lado especificado.
        
        Args:
            lado (float): Lado del cuadrado. Debe ser positivo.
            
        Raises:
            ValueError: Si el lado es negativo o cero.
        """
        if lado <= 0:
            raise ValueError("El lado debe ser un número positivo")
        self.lado = lado
    
    def calcular_area(self) -> float:
        """
        Calcula el área del cuadrado usando la fórmula lado².
        
        Returns:
            float: Área del cuadrado.
        """
        return self.lado ** 2
    
    def __str__(self) -> str:
        """Representación en cadena del cuadrado."""
        return f"Cuadrado(lado={self.lado})"
