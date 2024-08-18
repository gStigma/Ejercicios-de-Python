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


def run():
    n = int(input('Introduce cuantos numeros primos quieres: '))
    print(generar_primos(n))


if __name__ == '__main__':
    run()