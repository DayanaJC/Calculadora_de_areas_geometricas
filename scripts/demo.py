"""
Script de demostración para probar las clases de cálculo de áreas.
Este script muestra cómo usar las clases sin la interfaz gráfica.
"""

import sys
import os

# Agregar el directorio raíz al path para importar los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.logica.areas import Circulo, Triangulo, Rectangulo, Cuadrado


def demo_interactiva():
    """Demostración interactiva de las clases."""
    print("🧮 DEMO INTERACTIVA: Calculadora de Áreas")
    print("=" * 50)
    
    while True:
        print("\n📐 Seleccione una figura:")
        print("1. 🔵 Círculo")
        print("2. 🔺 Triángulo") 
        print("3. ▭ Rectángulo")
        print("4. ⬜ Cuadrado")
        print("5. ❌ Salir")
        
        try:
            opcion = input("\n👉 Ingrese su opción (1-5): ").strip()
            
            if opcion == "1":
                radio = float(input("📏 Ingrese el radio: "))
                circulo = Circulo(radio)
                area = circulo.calcular_area()
                print(f"✅ {circulo} → Área: {area:.4f} u²")
                
            elif opcion == "2":
                base = float(input("📏 Ingrese la base: "))
                altura = float(input("📏 Ingrese la altura: "))
                triangulo = Triangulo(base, altura)
                area = triangulo.calcular_area()
                print(f"✅ {triangulo} → Área: {area:.4f} u²")
                
            elif opcion == "3":
                largo = float(input("📏 Ingrese el largo: "))
                ancho = float(input("📏 Ingrese el ancho: "))
                rectangulo = Rectangulo(largo, ancho)
                area = rectangulo.calcular_area()
                print(f"✅ {rectangulo} → Área: {area:.4f} u²")
                
            elif opcion == "4":
                lado = float(input("📏 Ingrese el lado: "))
                cuadrado = Cuadrado(lado)
                area = cuadrado.calcular_area()
                print(f"✅ {cuadrado} → Área: {area:.4f} u²")
                
            elif opcion == "5":
                print("👋 ¡Hasta luego!")
                break
                
            else:
                print("❌ Opción inválida. Intente de nuevo.")
                
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")


if __name__ == "__main__":
    demo_interactiva()
