
def redondear(cantidad, decimales):
    cantidad_list = str(cantidad)
    cantidad_entera = int(cantidad)
    cantidad_decimal = '0.'
    j = 0
    dec = False
    for i in cantidad_list:
        if i == '.':
            dec = True
        elif j < decimales and dec:   
            cantidad_decimal = i + cantidad_decimal

    cantidad_entera = float(cantidad_entera) + float(cantidad_decimal)
            
    return cantidad_entera
        

    

def run():
    cantidad = float(input("Ingrese la cantidad: "))
    decimales = int(input("Ingrese la cantidad de decimales: "))
    print(f"La cantidad con los decimales es: {redondear(cantidad,decimales)} ")


if __name__ == '__main__':
    run()