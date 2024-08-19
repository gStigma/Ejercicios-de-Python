import math

def calcular_area_triangulo(v1, v2, v3):
    x1, y1 = v1
    x2, y2 = v2
    x3, y3 = v3
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

def longitud_lado(v1, v2):
    return math.sqrt((v2[0] - v1[0])**2 + (v2[1] - v1[1])**2)

def area_circunferencia_circunscrita(v1, v2, v3):
    area_triangulo = calcular_area_triangulo(v1, v2, v3)
    
    a = longitud_lado(v2, v3)
    b = longitud_lado(v1, v3)
    c = longitud_lado(v1, v2)
    
    R = (a * b * c) / (4 * area_triangulo)
    
    area_circunferencia = math.pi * R**2
    
    return area_circunferencia

def run():
    v1 = (0, 0)
    v2 = (3, 0)
    v3 = (0, 4)
    
    area_circunferencia = area_circunferencia_circunscrita(v1, v2, v3)
    print(f"El área de la circunferencia circunscrita es: {area_circunferencia:.2f}")

if __name__ == '__main__':
    run()
