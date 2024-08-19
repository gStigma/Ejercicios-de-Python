def suma_progresion(x,n):
    progrecion = 1
    for i in range(1,n+1):
        progrecion += x**i
    return progrecion

def  run():
    x =  int(input("introduce el  valor de  x: "))
    n =  int(input("introduce el  valor de  n: "))
    print(f"El resultado de la progrecion es: {suma_progresion(x,n)}")

if __name__ == '__main__':
    run()