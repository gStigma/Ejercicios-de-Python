def celsius_a_fahrenheit(n):
    F = (9/5)*n + 32
    return F

def run():
    n = float(input("Ingresa la temperatura en Celsius: "))
    print(f"Tu temperatura en Fahrenheit es: {celsius_a_fahrenheit(n)}")


if __name__ == "__main__":
    run()