import math

def calcular_area(v1, v2, v3):
    x1, y1 = v1
    x2, y2 = v2
    x3, y3 = v3
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

def puntos_en_borde(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return math.gcd(abs(x2 - x1), abs(y2 - y1)) + 1

def puntos_dentro_triangulo(v1, v2, v3):
    # Calcular el área del triángulo
    area = calcular_area(v1, v2, v3)
    
    b1 = puntos_en_borde(v1, v2)
    b2 = puntos_en_borde(v2, v3)
    b3 = puntos_en_borde(v3, v1)
    
    puntos_borde = b1 + b2 + b3 - 3
    
    # Usar el teorema de Pick: I = A - B/2 + 1
    puntos_interior = area - puntos_borde / 2 + 1
    
    return int(puntos_interior)

def run():
    v1 = (0, 0)
    v2 = (5, 0)
    v3 = (0, 5)
    puntos_interior = puntos_dentro_triangulo(v1, v2, v3)
    print(f"El número de puntos de coordenadas enteras dentro del triángulo es: {puntos_interior}")

if __name__ == '__main__':
    run()
