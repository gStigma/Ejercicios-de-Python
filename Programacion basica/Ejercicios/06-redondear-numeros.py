
def redondear(cantidad, decimales):
    cantidad_entera = ''
    for i in range(len(cantidad)):
        if cantidad[i] == '.':
            cantidad_entera =  cantidad_entera + cantidad[i:i+decimales+1]
            break
        else:
            cantidad_entera += cantidad[i]
    return float(cantidad_entera)
           

def run():
    cantidad = input("Ingrese la cantidad: ")
    decimales = input("Ingrese la cantidad de decimales: ")
    print(f"La cantidad con los decimales es: {redondear(cantidad,int(decimales))} ")


if __name__ == '__main__':
    run()