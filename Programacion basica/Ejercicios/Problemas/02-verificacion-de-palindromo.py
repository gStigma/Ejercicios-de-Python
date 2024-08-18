def invertir_cadena(s):
    new_cadena = ''
    for i in range(len(s)):
        v = s[len(s)-i-1:len(s)-i]
        new_cadena += str(v)
    return new_cadena


def es_palindormo(cadena):
    cadena_invertirda = invertir_cadena(cadena)
    if  cadena_invertirda == cadena:
        print("Es un palindromo")
    else:
        print("No es un palindromo")

def run():
    cadena = input("Introduce una cadena: ")
    es_palindormo(cadena)


if __name__ == '__main__':
    run()

