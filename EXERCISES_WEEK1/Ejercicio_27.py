    #Ejercicio 27 Cajero Automatico
saldo = 5000

while True:
    print("\nCajero Automático\n 1. para consultar saldo\n 2. para retirar dinero\n 3. para depositar dinero\n 4. para salir")
    operador= int(input("Ingrese la opción deseada (1-4): "))
    
    match operador:
        case 1:
            print(f"Su saldo actual es: ${saldo}")
        case 2:
            try:
                monto=float(input("Ingrese la cantidad de dinero que desea retirar: $"))
                if monto>saldo:
                    print("\nNo tienes suficiente dinero, asegurate de ingresar bien la cantidad")
                elif monto<=0:
                    print("no puedes retirar tan poquito")
                else:
                    saldo -= monto
                    print(f"\nAcabas de retirar ${monto}, y ahora solo te queda ${saldo}")
            except ValueError:
                print("ingresa un número")
        case 3:
            try:
                monto=float(input("Que cantidad va a depositar? $"))
                if monto<=0:
                    print("ERROR, no puedes depositar negativos o cero")
                else:
                    saldo += monto
                    print(f"Ahora has depositado ${monto}, y quedaste con ${saldo} en tu cuenta")
            except ValueError:
                print("solo números")
        case 4:
            print("Gracias por usar el Cajero Automático. ¡Hasta luego!")
            break
        case _:
            print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nOpción no válida. Ingrese una opción entre 1 y 4\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")