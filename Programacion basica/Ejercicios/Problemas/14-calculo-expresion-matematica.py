def calcular_expresion(x,n):
    if x >= 0:
        eq = x + ((x**n) / n) - ((x**(n+2)) / (n+2))
    else:
        eq =((x**(n+1))/(n+1)) - ((x**(n-1)) / (n-1))
    return eq

def run():
    x = float(input("Introduce x: "))
    n = int(input("Introduce n: "))
    print(f"El calculo es: {calcular_expresion(x,n)}")

if __name__ == '__main__':
    run()