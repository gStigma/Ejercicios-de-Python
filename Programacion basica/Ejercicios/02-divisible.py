
def es_divisible(a,b):
    return a%b == 0

def run():
    a = int(input("Ingresar un numero entero: "))
    b = int(input("Ingresa otro numero entero: "))
    if es_divisible(a,b):
        print(f"El numero {a} es divisible entre {b}")
    else:
        print(f"El numero {a} no es divisible entre {b}")


if __name__ == '__main__':
    run()