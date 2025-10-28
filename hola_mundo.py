mensaje = "¡Hola, Mundo!"
print(mensaje)

nombre= input("Ingresa tu nombre")
edad = int(input("Cual es tu edad: "))
altura= 1.75
activo=  False

if edad>=18:
    print("Tu nombre es: ", nombre, "Eres mayor de edad, y además tienes: ",edad, "años")
else:
    print(f"{nombre} Eres menor de edad")
