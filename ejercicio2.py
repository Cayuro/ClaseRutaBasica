# ---------------------------- NIVEL 2 ------------------------
    #Ejercicio 7: Mayor de edad
edad=int(input("Por favor ingrese su edad: "))
if edad < 18:
    print(f"Eres menor de edad, apenas tienes {edad} años.")
else:
    print(f"Eres mayor de edad, puedes votar.")

    #Ejercicio 8: Positivo, Negativo o cero.
nu= int(input("ingrese el numero que desea clasificar: "))
if nu < 0:
    print("Ese numero es negativo. ")
elif nu > 0:
    print("Ese numero es positivo")
else:
    print("Ese numero es igual a 0")

    #Ejercicio 9: Par o Impar:
numero=int(input("Ingresa el numero: "))
if numero%2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
    
    #Ejercicio 10: calculadora:
n1=int(input("Ingrese el primer número: "))
n2=int(input("Ingrese el segundo número: "))
op= input("Ingrese uno de los siguientes operadores: suma (+) , resta (-) , multiplicacion (*) , división (/) : ")
if op == '+':
    resultado= n1+n2
elif op == '-':
    resultado= n1-n2
elif op == '*':
    resultado= n1*n2
elif op == '/':
    resultado= n1/n2
else:
    resultado= "ERROR"
print(f"El resultado de la operación fue: {resultado}")

    #Ejercicio 11: Clasificador de notas
nota=int(input("Ingrese la nota"))
if nota < 3:
    print("Haz reprobado")
elif nota < 5:
    print("Acabas de aprobar, felicidades!")
elif nota == 5:
    print("Tu nota fue la mejor de la clase, lo hiciste excelente")
else:
    print("Creo que has ingresado una nota que no es")