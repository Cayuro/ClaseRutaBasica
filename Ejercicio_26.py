    # Ejercicio 26 - Carrito de Compras
#primero hacemos la lista de productos disponibles, con un diccionario para que a cada item se le defina un precio.
frutas = {
    "uva": 700,
    "fresa": 7000,
    "manzana": 2000,
    "sandia": 4000,
    "pera": 3200,
    "mango": 1600,
    "piña": 4500,
    "melocotón": 1800,
    "banano": 700,
    "naranja": 1000,
    "mandarina": 4300,
    "granadilla": 2300,
    "guayaba": 3700,
    "coco": 3200,
    "papaya": 5000
}

compras = {} 
total = 0   

print("\nFrutas disponibles y sus precios:")
for fruta, precio in frutas.items():
    print(f"{fruta.capitalize()}: ${precio}")

# Bucle para llenar el carrito
while True:
    fruta_elegida = input("Ingrese el nombre de la fruta (o escriba 'fin' para terminar): ").lower()
    if fruta_elegida == 'fin':
        break
    if fruta_elegida not in frutas:
        print(f"{fruta_elegida.capitalize()} no está disponible o el nombre es incorrecto.")
        continue
   
    # Bucle para pedir la cantidad, dentro del bucle de frutas, porque luego de la fruta se requiere la cantidad 
    # Con esto se logra que si la fruta es inválida, no se pida cantidad, y una vez se piden ambos reinicia el ciclo
    while True:
        try: #evita errores, si ingresan texto por ejemplo
            cantidad = int(input(f"¿Cuántas unidades de {fruta_elegida.capitalize()} desea llevar? "))
            if cantidad > 0: #si ingresan un número, además mayor que 0, ya queda bien asignada la cantidad, sale del bucle.
                break   #sale del bucle, sigue en el bucle de pedir frutas.
            else:#si no se cumple ese if, dice que no es positivo, por lo que es invalido, y este bucle vuelve a iniciar.
                print("La cantidad debe ser un número positivo.")
                
            
        except ValueError:
            print("Entrada no válida.")

    # aquí se añade la fruta y su cantidad, verificando primero si ya existe en el carrito, por si ingresa dos veces la misma fruta.
    if fruta_elegida in compras:
        cantidad_actual = compras[fruta_elegida]
    else:
        cantidad_actual = 0

    compras[fruta_elegida] = cantidad_actual + cantidad

    print(f"Se han añadido {cantidad} unidades de {fruta_elegida.capitalize()} al carrito.")

# Mostrar la factura
print("\n ---------- FACTURA ---------------")

if not compras: #no hay nada en la lista de compras
    print("El carrito está vacío.")
else:
    for fruta, cantidad in compras.items(): # en caso de que hayan compras, se inicia un bucle para mostrar cada fruta y cuanto le cuesta la cantidad
        precio_por_unidad = frutas[fruta]
        subtotal = precio_por_unidad * cantidad
        total += subtotal

        print(f"- {cantidad}x {fruta.capitalize()} @ ${precio_por_unidad:,} c/u: Subtotal ${subtotal:,}")

    print(f"\nTOTAL A PAGAR: ${total:,}") 
