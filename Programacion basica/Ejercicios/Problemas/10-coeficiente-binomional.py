def factorial(n):
    valor = 1
    if n > 0:
        for i in range(1,n+1):
            valor *= i
        return valor
    else:
        return 1

def coefiente_binominal(m,n):
     mf = factorial(m)
     nf = factorial(n)
     coeficiente = mf/(nf*factorial(m-n))
     return coeficiente

def run():
    m = int(input("Dame el valor de m: "))
    n = int(input("Dame el  valor de n: "))
    print(f"El valor del coeficiente es: {coefiente_binominal(m,n)}")

if __name__ == '__main__':
    run()