def cambiar_base(n, b):
    if b < 2:
        print("La base debe ser mayor o igual a 2.")
    
    if n == 0:
        return "0"
    
    caracteres = "0123456789ABCDEF"
    resultado = ""
    
    while n > 0:
        resultado = caracteres[n % b] + resultado
        n = int(n/b) 
    
    return resultado

def run():
    n = int(input("Introduce el número entero positivo (n): "))
    b = int(input("Introduce la base (b): "))
        
    if n < 0:
        print("El número debe ser entero positivo.")
        return
        
    resultado = cambiar_base(n, b)
    print(f"La representación de {n} en base {b} es {resultado}.")

if __name__ == '__main__':
    run()
