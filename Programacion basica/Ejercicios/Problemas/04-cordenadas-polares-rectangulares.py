import math

def polares_a_rectangulares(r,theta):
    x = r*math.cos(theta)
    y = r*math.sin(theta)
    print(f"Las cordenadas rectangulares son: ({x},{y})")

def run():
    r = float(input("Introduce el radio (cm/m/in): "))
    theta = float(input("Introduce theta (radianes): "))
    polares_a_rectangulares(r,theta)

if __name__ == '__main__':
    run()