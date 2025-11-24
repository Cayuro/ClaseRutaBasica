import csv
import os

# Manejo de archivo CSV para productos
def guardar_productos(ruta, productos):
    with open(ruta, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "brand", "category", "unit_price", "stock", "warranty"])
        for p in productos:
            writer.writerow([p["name"], p["brand"], p["category"], p["unit_price"], p["stock"], p["warranty"]])
    print(f"Inventory saved in {ruta}")

def cargar_productos(ruta):
    lista = []
    if not os.path.exists(ruta):
        return lista
    with open(ruta, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            n, b, c, u, s, w = row
            lista.append({"name": n, "brand": b, "category": c,
                          "unit_price": float(u), "stock": int(s), "warranty": int(w)})
    return lista

# CRUD
def agregar_producto(productos):
    def pedir_texto(msg):
        while True:
            val = input(msg).lower().strip()
            if any(ch.isdigit() for ch in val):
                print("Only letters allowed")
                continue
            return val
    
    nombre = pedir_texto("Product name: ")
    marca = pedir_texto("Brand: ")
    categoria = pedir_texto("Category: ")
    
    while True:
        try:
            precio = float(input("Unit price: "))
            stock = int(input("Stock: "))
            garantia = int(input("Warranty (months): "))
            break
        except ValueError:
            print("Numbers only")
    
    print("\nSummary ->", nombre, marca, categoria, precio, stock, garantia)
    if input("Confirm product? (Y/N): ").upper() == "Y":
        productos.append({"name": nombre, "brand": marca, "category": categoria,
                          "unit_price": precio, "stock": stock, "warranty": garantia})
        guardar_productos("productos.csv", productos)
        print("Product added")
    else:
        print("Cancelled")

def ver_productos(productos):
    if not productos:
        print("No products available")
        return
    print("\nInventory list:")
    for p in productos:
        print(f"{p['name']} | {p['brand']} | {p['category']} | ${p['unit_price']} | stock {p['stock']} | warranty {p['warranty']}")

def actualizar_producto(productos):
    nombre = input("Product to update: ").lower().strip()
    for p in productos:
        if p["name"].lower() == nombre:
            np = input("New price (enter to skip): ")
            ns = input("New stock (enter to skip): ")
            nw = input("New warranty (enter to skip): ")
            if np: p["unit_price"] = float(np)
            if ns: p["stock"] = int(ns)
            if nw: p["warranty"] = int(nw)
            guardar_productos("productos.csv", productos)
            print("Product updated")
            return
    print("Product not found")

def eliminar_producto(productos):
    nombre = input("Product to delete: ").lower().strip()
    for p in productos:
        if p["name"].lower() == nombre:
            if input("Confirm delete? (Y/N): ").upper() == "Y":
                productos.remove(p)
                guardar_productos("productos.csv", productos)
                print("Product deleted")
            else:
                print("Cancelled")
            return
    print("Product not found")
