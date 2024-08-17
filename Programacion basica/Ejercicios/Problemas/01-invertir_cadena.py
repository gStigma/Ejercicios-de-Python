
def invertir_cadena(cadena):
    new_cadena = ''
    for i in range(len(cadena)):
        v = cadena[len(cadena)-i-1:len(cadena)-i]
        new_cadena += str(v)
    print(f"Tu nueva cadena es: {new_cadena}")

def run():
    cadena = input("Introduce la cadena a intercambiar: ")
    invertir_cadena(cadena)

if __name__ == '__main__':
    run()