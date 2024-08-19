import math as m

def funciones_trigonometricas(theta):
    
    radianes = m.radians(theta)
    
    seno = m.sin(radianes)
    coseno = m.cos(radianes)
    tangente = m.tan(radianes)
    
    secante = 1 / coseno if coseno != 0 else float('inf')
    cosecante = 1 / seno if seno != 0 else float('inf')
    cotangente = 1 / tangente if tangente != 0 else float('inf')
    
    print(f"Ángulo (grados): {theta}")
    print(f"Seno (sin): {seno}")
    print(f"Coseno (cos): {coseno}")
    print(f"Tangente (tan): {tangente}")
    print(f"Secante (sec): {secante}")
    print(f"Cosecante (csc): {cosecante}")
    print(f"Cotangente (cot): {cotangente}")

def run():

    theta = float(input("Introduce el valor del ángulo en grados: "))
    funciones_trigonometricas(theta)

if __name__ == '__main__':
    run()
