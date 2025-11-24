def agregar_producto(inventario):
    while True:
        nombre = input("Nombre: ")
        if not nombre.replace(' ','').isalpha():
            continue
        while True:
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                break
            except ValueError:
                print("ingresa un precio o cantidad validos")
        inventario.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
        break
def mostrar_inventario(inventario):
    if not inventario:
        print("Inventario vacío")
        return
    print("Nombre | Cantidad | Precio")
    for item in inventario:
        print(f"{item['nombre']} | {item['cantidad']} | {item['precio']}")

def buscar_producto(inventario, nombre):
    encontrados = [p for p in inventario if nombre.lower() in p["nombre"].lower()]
    if not encontrados:
        print(f"No se encontró '{nombre}'")
    return encontrados

def actualizar_producto(inventario):
    nombre = input("Nombre del producto a actualizar: ").strip()
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            print("Deja vacío para omitir el cambio.")
            #pedir la cantidad
            nueva_cant = input("Nueva cantidad: ").strip()
            if nueva_cant != "":
                try:
                    nueva_cant = int(nueva_cant)
                    p["cantidad"] = nueva_cant
                except ValueError:
                    print("Cantidad inválida. No se modificó.")
            # ingresar el nuevo precio
            nuevo_precio = input("Nuevo precio: ").strip()
            if nuevo_precio != "":
                try:
                    nuevo_precio = float(nuevo_precio)
                    p["precio"] = nuevo_precio
                except ValueError:
                    print("Precio inválido. No se modificó.")

            print(f"Producto '{p['nombre']}' actualizado.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def eliminar_producto(inventario):
    nombre = input("ingrese el nombre del producto a eliminar: ")
    for i, p in enumerate(inventario):
        if p["nombre"].lower() == nombre.lower():
            inventario.pop(i)
            print(f"Producto '{nombre}' eliminado")
            return
    print(f"Producto '{nombre}' no encontrado")

def calcular_estadisticas(inventario):
    if not inventario:
        return {"unidades_totales": 0, "valor_total": 0, "producto_mas_caro": None, "producto_mayor_stock": None}

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["cantidad"] * p["precio"] for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }
