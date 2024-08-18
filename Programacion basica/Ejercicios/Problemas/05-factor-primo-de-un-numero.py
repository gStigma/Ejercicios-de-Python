def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generar_primos(n):
    primos = []
    num = 2  # Empezamos desde el primer número primo
    while len(primos) < n:
        if es_primo(num):
            primos.append(num)
        num += 1
    return primos


def factores_primos(n):
    primos = generar_primos(n)
    print("Los numeros primos son:")
    for i in primos:
        if n%i == 0:
            print(i)
    
def run():
    n = int(input("Introduce el numero: "))
    factores_primos(n)

if __name__ == '__main__':
    run()