#---------------------- NIVEL 3 ---------------------
    #Ejercicio 13 contar del 1 al 10
i=1
while True:
    if i>10:
        break
    print(i)
    i+=1

    #Ejercicio 14  sumatoria 1 al n
print("___________--------------_________________")
print("Ahora haremos la sumatoria desde 1 hasta n")
n=int(input("Ingrese hasta el número que desea hacer la sumatoria: "))
sumatoria=0
for i in range(n+1):
    sumatoria= sumatoria+i
print(f"si sumas los números hasta {n} el resultado es: {sumatoria}")


    #Ejercicio 15  tabla de multiplicar
print("___________--------------_________________")
num=int(input("Ingrese hasta el número del que desea ver la tabla de multiplicar: "))

for i in range(11):
    opera= i*num
    print(f" {i} x {num} = {opera}")

    #Ejercicio 16  contador regresivo con while
n=int(input("Ingrese el número desde donde empieza la cuenta regresiva: "))

while n>0:
    print(n)
    n-=1

    #Ejercicio 17   adivina el numero random
import random
print("___________--------------_________________")
print("Ahora vamos a jugar a adivinar números, en el rango que elijas\n puedes escribir (salir) para acabar")
inicio= int(input("En donde quieres empezar (rango de número a adivinar): "))
fin= int(input("En donde quieres terminar (rango del número a adivinar): "))
numero_random= random.randint(inicio,fin)
intento=0
while True:
    numero= (input("Adivina el número (o escribe (Salir) para rendirte): "))

    if numero.lower() == "salir":
        print(f"es una lastima que hayas decidido rendirte.")
        break
    try:
        numero= int(numero)
        intento+=1
        if numero == numero_random:
            print(f"EXCELENTE, FELICIDADES, has adivinado el número aleatorio.")
            break
        elif numero < numero_random:
            print(f"el numero {numero} es menor que el que buscas.")
        elif numero > numero_random:
            print(f"el número {numero} es mayor que el buscado.")
    
    except ValueError:
        print("El valor ingresado no fue salir, ni tampoco un número, intenta de nuevo")

    #Ejercicio 18   sumar hata usuario escriba 0
print("________________---_______________")
n1= int(input("Ahora vamos a sumar, ingresa un numero: "))
sumado=n1
while True:
    n2=int(input("Ahora cuanto le quieres sumar (o 0 para ver resultado): "))
    sumado= sumado+n2
    if n2 == 0:
        print(f"la suma de todos estos números es: {sumado}")
        break
