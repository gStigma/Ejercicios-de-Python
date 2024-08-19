import math as r

def area_triangulo(a,b,c):
    p = (a+b+c)/2
    area = r.sqrt(p*(p-a)*(p-b)*(p-c))
    return area

def run():
    a = int(input("Introduce a: "))
    b = int(input("Introduce b: "))
    c = int(input("Introduce c: "))
    print(f"El area del triangulo es: {area_triangulo(a,b,c)}")

if __name__ == '__main__':
    run()