# Función para calcular el área de un rectángulo
def f(a, b):
    result = a * b
    return result
from library import calcular_area_rectangulo, calcular_area_triangulo

def main():
    # Ingresar datos para el rectángulo
    base_rectangulo = float(input("Ingrese la base del rectángulo: "))
    altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))
    area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
    print("Área del rectángulo:", area_rectangulo)

    # Ingresar datos para el triángulo
    base_triangulo = float(input("Ingrese la base del triángulo: "))
    altura_triangulo = float(input("Ingrese la altura del triángulo: "))
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    print("Área del triángulo:", area_triangulo)

main()