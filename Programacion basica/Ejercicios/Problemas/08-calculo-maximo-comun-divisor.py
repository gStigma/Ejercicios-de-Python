def mcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def run():
    a = int(input("Introduce el  primer numero: "))
    b = int(input("Introduce el segundo número: "))
    print(f"El máximo común divisor de {a} y {b} es {mcd(a,b)}.")

if __name__ == '__main__':
    run()