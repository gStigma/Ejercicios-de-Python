import math

def calcular_valor(x):
    eq = (x**5) *  (math.exp(2*x)-1)
    return eq

def run():
    x = float(input("Introduce x: "))
    if x != 0:
        print(f"El valor es: {calcular_valor(x)}")
    else:
        print("x no puede  ser 0")

if __name__ == '__main__':
    run()