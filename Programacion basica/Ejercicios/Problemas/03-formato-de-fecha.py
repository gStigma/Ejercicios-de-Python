def formato_de_fecha(dia,mes,anio):
    formato = f"{dia}/{mes}/{anio[2:4]}"
    print(formato)

def run():
    dia = input("Introduce el el dia: ")
    mes = input("Introduce el el mes: ")
    anio = input("Introduce el el anio: ")
    formato_de_fecha(dia,mes,anio)

if __name__ == '__main__':
    run()
