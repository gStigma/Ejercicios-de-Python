def romano_a_arabigo(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    anterior = 0

    for letra in romano:
        valor = valores[letra]

        if valor > anterior:
            # Se resta el doble del valor anterior si es menor (casos como IV = 4)
            total += valor - 2 * anterior
        else:
            total += valor

        anterior = valor

    return total

def run():
    prueba_romanos = ["LXXXVI", "CCCXIX", "MCCLIV"]
    
    for romano in prueba_romanos:
        arábigo = romano_a_arabigo(romano)
        print(f"El número romano {romano} es equivalente a {arábigo} en numeración arábiga.")

    # Opción para que el usuario introduzca un número romano
    romano = input("Introduce un número romano (hasta diez caracteres): ").upper()
    if len(romano) > 10:
        print("La cadena introducida es demasiado larga.")
    else:
        arábigo = romano_a_arabigo(romano)
        print(f"El número romano {romano} es equivalente a {arábigo} en numeración arábiga.")

if __name__ == '__main__':
    run()
