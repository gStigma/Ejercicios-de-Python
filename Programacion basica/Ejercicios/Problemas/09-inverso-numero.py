def inverso_numero(n):
    inv = ''
    for i in range(len(n)):
        inv += n[len(n)-i-1:len(n)-i]
    return int(inv)

def run():
    numero = input("Introduce  el numero a invertir: ")
    print(f"Tu numero invertido es {inverso_numero(numero)}")


if __name__ == '__main__':
    run()