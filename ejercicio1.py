
#---------------------- NIVEL 1 ------------------------------------
    # primer ejercicio: pide nombre y edad
nombre= input("Por favor ingresa tu nombre: ")
edad= int(input("Por favor ingresa tu edad: "))
print(f"Hola {nombre} es un gusto conocerte, y saber que tienes {edad} años: ")
print()
    # Segundo ejercicio: suma dos numeros
a, b= int(input("Ingresa primer numero a sumar: ")), int(input("Ingresa el segundo numero: "))
print(a+b)
print()
    # Tercer ejercicio: Area del triangulo
altura= float(input("Cual es la altura del triangulo:  "))
base = float(input("Ingrese la base del triangulo:  "))
Area = (base*altura)/2
print(f"El Area del triangulo es {Area}")
print()
    # Cuarto ejercicio: Conversor de Celcius a Fahrenheit
Grados= int(input("Ingresa los grados en celcius: "))
conversion= (Grados * 9/5) + 32
print(conversion)
print()
    # Ejercicio 5: Tipo de dato
print(type(nombre)," ", type(edad)," ", type(a)," ", type(b)," ", type(altura)," ", type(base)," ", type(Area))
print()
    # Ejercicio 6: Tipo de dato
edad_futura= edad+10
print(f"""{nombre} ya sabemos que tu edad es de {edad} años y 
para cuando acabes la universidad vas a tener {edad_futura} años
""")
