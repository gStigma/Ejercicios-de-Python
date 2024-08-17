def es_digito(caracter):
    n = ["0", "1", "2", "3", "4", "5", "6", "7" ,"8" ,"9"]
    return(caracter in n)
    

def run():
    caracter = input("Introduce el caracter: ")
    if es_digito(caracter):
        print("El caracter se encuentra entre el 0 y 9")
    else:
        print("El caracter no se encuentra entre el 0 y 9")


if __name__ == '__main__':
    run()