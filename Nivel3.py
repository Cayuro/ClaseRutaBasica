#---------------------- NIVEL 3 ---------------------
    #Ejercicio 13 contar del 1 al 10
'''
i=1
while True:
    if i>10:
        break
    print(i)
    i+=1

    #Ejercicio 14  sumatoria 1 al n
n=int(input("Ingrese hasta el número que desea hacer la sumatoria: "))
sumatoria=0
for i in range(n+1):
    sumatoria= sumatoria+i
print(f"si sumas los números hasta {n} el resultado es: {sumatoria}")


    #Ejercicio 15  tabla de multiplicar
num=int(input("Ingrese hasta el número del que desea ver la tabla de multiplicar: "))

for i in range(10):
    opera= i*num
    print(f" {i} x {num} = {opera}")
'''
    #Ejercicio 16  contador regresivo con while
n=int(input("Ingrese el número desde donde empieza la cuenta regresiva: "))

while n>0:
    print(n)
    n-=1
    #Ejercicio 17   adivina el numero random

    #Ejercicio 18   sumar hata usuario escriba 0
