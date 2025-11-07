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
    result= n1+n2
elif op == '-':
    result= n1-n2
elif op == '*':
    result= n1*n2
elif op == '/':
    result= n1/n2
else:
    result= "ERROR"
    print("Este no es un operador aritmetico")
print(f"El resultado de la operación fue: {resultado}")

    #Ejercicio 11: Clasificador de notas
nota=int(input("Ingrese la nota"))
if ((nota>0) and (nota < 3)):
    print("Haz reprobado")
elif ((nota>0) and (nota < 5)):
    print("Acabas de aprobar, felicidades!")
elif nota == 5:
    print("Tu nota fue la mejor de la clase, lo hiciste excelente")
else:
    print("Creo que has ingresado una nota que no es")

    #Ejercicio 12: Comparador de tres numeros
num1=int(input("Ingresa el primer número: "))
num2=int(input("Ingresa el segundo número: "))
num3=int(input("Ingresa el tercer número: "))

if num1>=num2 and num1>=num3:
    mayor= num1
elif num2>=num1 and num2>=num3:
    mayor=num2
else:
    mayor=num3
print(f"el numero MAYOR de estos tres es {mayor}")
if num1<=num2 and num1<=num3:
    menor= num1
elif num2<=num1 and num2<=num3:
    menor=num2
else:
    menor=num3
print(f"el numero MENOR de estos tres es {menor}")
