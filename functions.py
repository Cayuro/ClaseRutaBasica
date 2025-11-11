'''def mostrar_bienvenida(name= "Coder"):
    print(f"Hola {name}, Bienvenido!\n" *5)
mostrar_bienvenida("Juanes")

    #otra forma
def bienvenida(name="Coders"):
    return f"Hola {name}, bienvenido"
print(bienvenida())
'''
'''
    #un poco más largo
def saludos_estudiante(name='Coder',edad='20'):
    print(f"Hola mi nombre es {name}, y tengo {edad}años.")
saludos_estudiante()
saludos_estudiante(edad=22, name="Juan Esteban G")

    #definición Suma
def sumar(a,b): 
    return a+b
print(sumar(5,7))
    #definición multiplicar
def multiplicar(x,y):
    return x*y
print(multiplicar(5,3))
    #Otra forma más larga
def multiplica(a,b):
    resultado = a*b
    return resultado
print(multiplica(7,8))

    #subiendo un poco, Crear función que diga si es par o impar
def pares(x):
    if x % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
n=int(input("Ingrese un número cualquiera, para saber si es par o impar: "))
p=int(input("Ingrese un número cualquiera, para saber si es par o impar: "))
pares(n)
pares(p)
print()
'''
'''
    #un poco más de nivel, pidiendo a la persona los números y en una lista para evaluar iterando en la lista
def par_impar():
    list_number=[]
    n=int(input("cúantos números quieres evaluar si son pares o impares: "))
    for i in range(n):
        num1=int(input(f"Ingrese el {i+1} número a evaluar: "))
        list_number.append(num1)
    for x in list_number:
        if x % 2 ==0:
            print(f"* {x} Es par")
        else:
            print(f"* {x} es impar")

par_impar()

    #un promedio sencillo
def promedio(n1,n2,n3,n4):
    resultado= (n1+n2+n3+n4)/4
    return resultado

print(promedio(1,2,5,18))
'''

'''
    #un promedio un poco más complejo
def promedio(num):
    return (sum(num)/len(num))
def getData():
    num=[]
    for i in range(4):
        num.append(int(input("Ingrese un número: ")))
    return promedio(num)

print(getData())
'''
'''
    #Ejercicio
lista= []
for i in range(10):
    nombre=input("Ingresa el nombre: ")
    if nombre == "Andres":
        break
    lista.append(nombre)
print(lista)
'''
    # Otra forma de hacer el ejercicio

nombres=[]
while not("andres" in nombres or len(nombres)==10):
    nombres.append(input("Introduzca su nombre: ")).lower()
    
