def maximo(a,b):
    if a>b:
        return a
    else:
        return b

def run():
    a = int(input("Introduce el primer numero: "))
    b = int(input("Introduce el segundo numero: "))
    print(f"El numero mayor es: {maximo(a,b)} ")

if __name__ == '__main__':
    run()

