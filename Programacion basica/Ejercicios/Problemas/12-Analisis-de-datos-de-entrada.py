def ordenamiento(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[min_idx] > lista[j]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def numero_mayor(lista):
    print(f"El mayor numero  es: {lista[len(lista)-1]} ")
    print(f"El menor numero  es: {lista[0]} ")

def suma_media(lista):
    valor = 0
    for i in  lista:
        valor += i
    print(f"La suma  de los datos: {valor}")
    valor = valor/len(lista)
    print(f"La media de los datos: {valor}")


def lista_numeros(n):
    lista = []
    for i in range(n):
        num = int(input(f"Introduce el {i+1} número: "))
        lista.append(num)
    valores_ordenados = ordenamiento(lista)
    numero_mayor(valores_ordenados)
    suma_media(valores_ordenados)



def run():
    n = int(input("¿Cuántos números quieres introducir? "))
    lista_numeros(n)

if __name__ == '__main__':
    run()
