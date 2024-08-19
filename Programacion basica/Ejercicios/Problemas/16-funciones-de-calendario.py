def obtener_dia_por_inicial(letra):
    letra = letra.upper()
    dias = {
        'L': 'Lunes',
        'M': 'Martes',
        'X': 'Miércoles',
        'J': 'Jueves',
        'V': 'Viernes',
        'S': 'Sábado',
        'D': 'Domingo'
    }
    
    if letra in dias:
        return dias[letra]
    else:
        return "Letra no válida. Por favor, introduce una letra válida."

def dias_del_mes(mes, año):
    if mes == 2:
        return 29 if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)) else 28
    elif mes in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def run():
    # Obtener el nombre del día a partir de la letra inicial
    letra = input("Introduce la letra inicial del día de la semana (L, M, X, J, V, S, D): ")
    dia_semana = obtener_dia_por_inicial(letra)
    print(f"Día de la semana: {dia_semana}")
    
    mes = int(input("Introduce el número del mes (1-12): "))
    año = int(input("Introduce el año (e.g., 2024): "))
        
    if 1 <= mes <= 12:
        print(f"El mes {mes} del año {año} tiene {dias_del_mes(mes, año)} días.")
    else:
        print("Por favor, introduce un mes válido (1-12).")
    

if __name__ == '__main__':
    run()
