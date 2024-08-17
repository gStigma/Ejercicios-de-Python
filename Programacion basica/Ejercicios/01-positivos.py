
def determainar_positividad(n):
    if n > 0:
        return 'P'
    else:
        return 'N'

def run():
    n = input("Ingrese un numero entero: ")
    resultado = determainar_positividad(int(n))
    print(resultado)

if __name__ == '__main__':
    run()