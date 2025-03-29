import math

def area_cuadrado(lado):
    return lado ** 2

def area_circulo(radio):
    return math.pi * radio ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rectangulo(base, altura):
    return base * altura

def area_hexagono(lado):
    return (3 * math.sqrt(3) * lado ** 2) / 2

def menu():
    print("Seleccione la figura para calcular el área:")
    print("1. Área de un cuadrado")
    print("2. Área de un círculo")
    print("3. Área de un triángulo")
    print("4. Área de un rectángulo")
    print("5. Área de un hexágono")
    print("0. Salir")

    opcion = int(input("Ingrese el número de la opción deseada: "))
    
    if opcion == 1:
        lado = float(input("Ingrese el lado del cuadrado: "))
        print(f"El área del cuadrado es: {area_cuadrado(lado)}")
    elif opcion == 2:
        radio = float(input("Ingrese el radio del círculo: "))
        print(f"El área del círculo es: {area_circulo(radio)}")
    elif opcion == 3:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print(f"El área del triángulo es: {area_triangulo(base, altura)}")
    elif opcion == 4:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        print(f"El área del rectángulo es: {area_rectangulo(base, altura)}")
    elif opcion == 5:
        lado = float(input("Ingrese el lado del hexágono: "))
        print(f"El área del hexágono es: {area_hexagono(lado)}")
    elif opcion == 0:
        print("Saliendo del programa.")
        exit()
    else:
        print("Opción no válida.")
    
    menu()

