    #Ejercicio 29 Calculadora avanzada (usar funciones)
def sumar(num1, num2):
    return num1 + num2
def restar(num1, num2):
    return num1 - num2
def multiplica(num1, num2):
    return num1*num2
def divide(num1, num2):
    if num2 == 0:
        return "Error: No está definida la división entre 0"
    return num1 / num2
def potencia(num1, num2):
    return num1**num2

while True:
    print("\n Calculadora Avanzada\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Potencia\n6. Salir")
    try:
        opcion= int(input("Seleccione una opción (1-6): "))
        if opcion < 1 or opcion > 6:
            raise ValueError("Opción inválida")
    except ValueError:
        print("Entrada invalida, ingrese numero entre 1 y 6")
        continue
    
    if opcion == 6:
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break
    
    elif opcion in [1, 2, 3, 4, 5]:
        while True:
            try: 
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Entrada inválida")
                continue
            
            match opcion:
                case 1:
                    resultado = sumar(num1, num2)
                case 2:
                    resultado = restar(num1, num2)
                case 3:
                    resultado = multiplica(num1, num2)
                case 4:
                    resultado = divide(num1, num2)
                case 5:
                    resultado = potencia(num1, num2)
            print(f"El resultado es: {resultado}")
            break