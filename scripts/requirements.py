"""
Script para generar el archivo requirements.txt
"""

def generar_requirements():
    """Genera el archivo requirements.txt con las dependencias necesarias."""
    requirements = [
        "PyQt6>=6.4.0",
        "# Dependencias para desarrollo (opcional)",
        "# pytest>=7.0.0  # Para testing",
        "# black>=22.0.0   # Para formateo de código",
        "# flake8>=4.0.0   # Para linting"
    ]
    
    with open("requirements.txt", "w", encoding="utf-8") as f:
        for req in requirements:
            f.write(req + "\n")
    
    print("✓ Archivo requirements.txt generado correctamente")
    print("\nPara instalar las dependencias, ejecuta:")
    print("pip install -r requirements.txt")


if __name__ == "__main__":
    generar_requirements()
