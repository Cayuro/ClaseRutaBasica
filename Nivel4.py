#-----------------------------NIVEL 4 ---------------------------------------

# ------------------------ FRUTAS ---------------------------

    #Ejercicio 19 lista de frutas 
Frutas=["manzana", "pera", "mango"] 
print(f"estas son las frutas que tienes: {Frutas}")

    #Ejercicio 20 Agregar y eliminar frutas 
agregadas= int(input("Que cantidad de frutas vas a añadir: ")) 
for i in range(agregadas): 
    nuevafruta= input("Ingresa la fruta que quieres agregar: ") 
    Frutas.append(nuevafruta.lower()) 
print(f"ahora tienes las siguientes frutas: {Frutas}") 
sustraidas= int(input("qué cantidad de frutas deseas eliminar: ")) 
for i in range(sustraidas): 
    sustraida1= input("nombre de la fruta que deseas sustraer: ") 
    Frutas.remove(sustraida1.lower()) 
print(f"ahora tienes las siguientes frutas: {Frutas}")

    #Ejercicio 21 Buscar un elemento de lista 
buscar=input("Ingresa la fruta que deseas buscar en tu lista, y te diré la posición: ")

if buscar in Frutas: 
    print(f"la fruta {buscar} está en la lista") 
    for i in range(len(Frutas)): 
        if buscar== Frutas[i]: 
            buscar = Frutas.index(buscar) 
            print(f"en la posición {buscar+1}") 
else: 
    print(f"la {buscar} no está en la lista")

    #------------------------------  Numeros -----------------

    #Ejercicio 22 lista de numeros y promedio
Numeros=[] 
suma=0
cantidad= int(input("¿cuantos numeros quieres ingresar a la lista? ")) 
for i in range(cantidad): 
    num1= int(input(f"ingrese el {i+1} número: ")) 
    Numeros.append(num1)
    suma= suma+num1

promedio=   suma/len(Numeros)
print(f"tu lista es la siguiente: {Numeros}\n y el promedio es: {promedio}")
    
    #Ejercicio 23 solo guarda los pares
n_pares= []
for i in range(len(Numeros)):
    if Numeros[i] % 2 == 0:
        n_pares.append(Numeros[i])
print(f"la lista con solo los números pares es la siguiente: {n_pares}")

    #Ejercicio 24 elimina duplicados
# Iterar hacia atrás (desde el penúltimo elemento hasta el primero)
for i in range(len(Numeros) - 2, -1, -1):
    # Iterar desde el elemento actual (i) hacia atrás
    for j in range(len(Numeros) - 1, i, -1):
        # Si encuentra un duplicado
        if Numeros[i] == Numeros[j]:
            # Elimina el duplicado (el que tiene el índice mayor, j)
            Numeros.pop(j)
print(f"la lista sin duplicados es: {Numeros}")


