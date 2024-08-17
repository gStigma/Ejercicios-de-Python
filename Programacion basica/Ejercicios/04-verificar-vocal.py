def es_vocal(caracter):
    vocales = ['a','e','i','o','u']
    return (caracter in vocales)

def run():
    caracter = input("Introduce el caracter: ")
    if es_vocal(caracter):
        print("El caracter es una vocal")
    else:
        print("El caracter no es una vocal")


if __name__ == '__main__':
    run()