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
    "papaya": 6000
}

compras = {} 
total = 0   

print("\nFrutas disponibles y sus precios:")
for fruta, precio in frutas.items():
    print(f"- {fruta.capitalize()}: ${precio}")

# Bucle para llenar el carrito
while True:
    print("-" * 30)

    # 3. Pedir la fruta
    fruta_elegida = input("Ingrese el nombre de la fruta (o escriba 'fin' para terminar): ").lower()

    # Condición de salida
    if fruta_elegida == 'fin':
        break

    # 4. Validar si la fruta existe (Ahora se usa 'frutas')
    if fruta_elegida not in frutas:
        print(f"❌ '{fruta_elegida.capitalize()}' no está disponible o el nombre es incorrecto.")
        continue # Vuelve al inicio del bucle

    # 5. Pedir la cantidad
    while True:
        try:
            cantidad = int(input(f"¿Cuántas unidades de {fruta_elegida.capitalize()} desea llevar? "))
            if cantidad <= 0:
                print("⚠️ La cantidad debe ser un número positivo.")
                continue
            break # Sale del bucle de cantidad si es válido
        except ValueError:
            print("⚠️ Entrada no válida. Por favor, ingrese un número entero.")

    # 6. Añadir/Actualizar el carrito (Ahora se usa 'compras')
    # Si la fruta ya está, se suma la nueva cantidad. Si no está, se agrega.
    cantidad_actual = compras.get(fruta_elegida, 0)
    compras[fruta_elegida] = cantidad_actual + cantidad

    print(f"✅ Se han añadido {cantidad} unidades de {fruta_elegida.capitalize()} al carrito.")

# ---------------------------------------------
# 7. CÁLCULO Y RESUMEN FINAL
# ---------------------------------------------

print("\n\n--- 🧾 FACTURA Y TOTAL ---")

# Se usa 'compras'
if not compras:
    print("El carrito está vacío.")
else:
    # Se usa 'frutas' para obtener el precio
    for fruta, cantidad in compras.items():
        precio_por_unidad = frutas[fruta]
        subtotal = precio_por_unidad * cantidad
        total += subtotal # Se usa 'total'
        
        print(f"- {cantidad}x {fruta.capitalize()} @ ${precio_por_unidad:,} c/u: Subtotal ${subtotal:,}")

    print("-" * 40)
    print(f"TOTAL FINAL A PAGAR: ${total:,}") # Se usa 'total'
    print("-" * 40)