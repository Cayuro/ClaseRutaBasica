'''
print ("ingresar tu nombre =>")
nombre  =  input ( )
print( "ingresar tu apellido =>")
apellido  =  input ( )
print( "ingresar tu edad =>")
edad  =  input ( )
        
print (f"hola soy {nombre} {apellido} y tengo  {edad} años")

#hola esto es un entero
entero = int(input("Ingresa un numero entero "))
negativo = -entero
print(negativo)
multiplica= negativo*6
print(multiplica)
multiplica= -negativo*6
print(multiplica)


nombre = "Juan Esteban"
for i in range(0, 13, 2):
    print(nombre + " posición " +str(i))

edad= 18
edad_necesaria= 25
while edad<=edad_necesaria:
    print(edad)
    edad= edad+1
  
   '''
#Lista de Numeros, ingresada por el usuario, y organizada
Arreglo= [8,6,9]
n=int(input("Ingrese el numero de elementos: "))

for i in range(n):
    num= int(input(f"Ingrese el número en la posición {i+1}: "))
    Arreglo.append(num)

print(Arreglo)

temp=None
for i in range(n+3):
    for j in range(0, (n+3)-i-1):
        if Arreglo[j]>Arreglo[j+1]:
            temp=Arreglo[j]
            Arreglo[j]=Arreglo[j+1]
            Arreglo[j+1]=temp
            #Arreglo[j], Arreglo[j + 1] = Arreglo[j + 1], Arreglo[j]

print(f"El arreglo organizado es {Arreglo}")
print(f"El número menor de entre los que ingresaste es {Arreglo[0]}")
print(f"El número mayor de entre los que ingresaste es {Arreglo[n-1]}")



inicio=0
fin=n

Arreglo= []
n=int(input("Ingrese el numero de elementos: "))

for i in range(n):
    num= int(input(f"Ingrese el número en la posición {i+1}: "))
    Arreglo.append(num)
