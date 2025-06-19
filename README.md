#  Calculadora de Áreas Interactiva - PyQt6

##  Integrantes
Javier Curi Dayana  
Ricaldi Solis Maylon

Una aplicación de escritorio **completamente interactiva** desarrollada con PyQt6 y Programación Orientada a Objetos (POO) para calcular áreas de figuras geométricas en tiempo real.

##  Características Principales

**Cálculo automático en tiempo real** - Los resultados se actualizan mientras escribes  
**Interfaz moderna e intuitiva** - Diseño colorido y fácil de usar  
**Historial de cálculos** - Guarda todos tus cálculos realizados  
**Validación instantánea** - Detecta errores al momento  
**4 figuras geométricas** - Círculo, Triángulo, Rectángulo, Cuadrado  

##  Instalación y Ejecución

### 1. Instalar PyQt6
powershell
pip install PyQt6



### 2. Ejecutar la aplicación
powershell
python app.py



### 3. Probar en consola (opcional)
powershell
python scripts/demo.py



##  Cómo Usar

1. **Abrir la aplicación** ejecutando python app.py  
2. **Ingresar valores** en cualquiera de las 4 calculadoras  
3. **Ver resultados instantáneos** - Se calculan automáticamente  
4. **Revisar historial** - Todos los cálculos se guardan abajo  
5. **Limpiar historial** - Botón rojo para borrar todo  

##  Figuras Soportadas

###  Círculo
**Campo:** Radio  
**Fórmula:** π × r²  
**Ejemplo:** Radio = 5 → Área = 78.5398 u²  

###  Triángulo  
**Campos:** Base y Altura  
**Fórmula:** (base × altura) ÷ 2  
**Ejemplo:** Base = 10, Altura = 8 → Área = 40.0000 u²  

###  Rectángulo
**Campos:** Largo y Ancho  
**Fórmula:** largo × ancho  
**Ejemplo:** Largo = 12, Ancho = 6 → Área = 72.0000 u²  

###  Cuadrado
**Campo:** Lado  
**Fórmula:** lado²  
**Ejemplo:** Lado = 7 → Área = 49.0000 u²  

##  Estructura del Proyecto

![image](https://github.com/user-attachments/assets/438b2e49-4075-4d8e-a1aa-37e49e0a5c6c)

##  Características Técnicas

### **POO Implementada:**
✅ **Clases separadas** para cada figura geométrica  
✅ **Constructores con validación** de parámetros positivos  
✅ **Método calcular_area()** en cada clase  
✅ **Encapsulación** completa de datos y comportamiento  
✅ **Manejo de excepciones** personalizado  

### **Interfaz Interactiva:**
✅ **Cálculo en tiempo real** - Sin necesidad de botones  
✅ **4 calculadoras simultáneas** - Una para cada figura  
✅ **Diseño responsive** - Se adapta al tamaño de ventana  
✅ **Colores distintivos** - Cada figura tiene su color  
✅ **Historial persistente** - Guarda todos los cálculos  

### **Validaciones Robustas:**
✅ **Solo números positivos** - Rechaza valores negativos o cero  
✅ **Detección de errores** - Muestra mensajes claros  
✅ **Campos obligatorios** - No calcula con campos vacíos  
✅ **Formato numérico** - Acepta decimales y enteros  

##  Capturas de Funcionalidad

La aplicación muestra:  
**4 calculadoras en grid 2x2** - Organizadas visualmente  
**Campos de entrada intuitivos** - Con placeholders descriptivos  
**Resultados en tiempo real** - Se actualizan al escribir  
**Historial scrolleable** - Lista todos los cálculos realizados  
**Menú completo** - Con opciones de ayuda y salida  

##  Ejemplos de Uso

### Círculo:
1. Escribir "5" en el campo Radio  
2. Ver automáticamente: "Área: 78.5398 u²"  
3. Aparece en historial: " Círculo (r=5): 78.5398 u²"  

### Triángulo:
1. Escribir "10" en Base y "8" en Altura  
2. Ver automáticamente: "Área: 40.0000 u²"  
3. Aparece en historial: " Triángulo (b=10, h=8): 40.0000 u²"  

### Rectángulo:
1. Escribir "12" en Largo y "6" en Ancho  
2. Ver automáticamente: "Área: 72.0000 u²"  
3. Aparece en historial: " Rectángulo (l=12, a=6): 72.0000 u²"  

### Cuadrado:
1. Escribir "7" en el campo Lado  
2. Ver automáticamente: "Área: 49.0000 u²"  
3. Aparece en historial: " Cuadrado (l=7): 49.0000 u²"  

##  Desarrollo

### Agregar Nueva Figura:
1. Crear clase en src/logica/areas.py  
2. Agregar calculadora en src/vista/calculadora_widget.py  
3. Conectar eventos y validaciones  

### Personalizar Estilos:
Modificar colores en aplicar_estilo_grupo()  
Cambiar fuentes en los StyleSheets  
Ajustar layouts en setupUI()  

##  Contribuir

¡Las contribuciones son bienvenidas!
 Agregar más figuras (pentágono, hexágono, etc.)
 Mejorar el diseño visual
 Añadir gráficos de las figuras
 Exportar resultados a archivo
 Crear tests unitarios

**Desarrollado usando PyQt6, Python y mucha interactividad**
