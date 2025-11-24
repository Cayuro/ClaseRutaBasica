import csv
import os
from datetime import datetime

# ==================== ARCHIVO CSV PARA VENTAS ====================

def cargar_ventas(ruta):
    """Carga todas las ventas desde un archivo CSV"""
    lista = []
    if not os.path.exists(ruta):
        return lista
    
    with open(ruta, "r") as f:
        reader = csv.reader(f)
        next(reader)  # saltar encabezado
        for row in reader:
            cliente, tipo, producto, cantidad, fecha, descuento, total = row
            lista.append({
                "customer": cliente,
                "customer_type": tipo,
                "product": producto,
                "quantity": int(cantidad),
                "date": fecha,
                "discount": float(descuento),
                "total": float(total)
            })
    return lista

def guardar_ventas(ruta, ventas):
    """Guarda todas las ventas en un archivo CSV"""
    with open(ruta, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["customer", "customer_type", "product", "quantity", "date", "discount", "total"])
        for v in ventas:
            writer.writerow([v["customer"], v["customer_type"], v["product"],
                             v["quantity"], v["date"], v["discount"], v["total"]])
    print(f"Sales saved in {ruta}")

# ==================== REGISTRAR UNA VENTA ====================

def registrar_venta(productos, ventas):
    """Registrar una nueva venta con validaciones básicas"""
    cliente = input("Customer name: ").lower().strip()
    
    print("\nCustomer types:")
    print("1. regular (0% discount)")
    print("2. vip (10% discount)")
    print("3. wholesale (15% discount)")
    
    while True:
        opcion = input("Select type (1-3): ").strip()
        if opcion in ["1", "2", "3"]:
            break
        print("Invalid option, choose 1, 2 or 3")
    
    tipos = {"1": "regular", "2": "vip", "3": "wholesale"}
    tipo_cliente = tipos[opcion]
    
    if not productos:
        print("No products available")
        return
    
    print("\nAvailable products:")
    for p in productos:
        print(f"{p['name']} | brand: {p['brand']} | price: ${p['unit_price']} | stock: {p['stock']}")
    
    nombre_producto = input("\nProduct name to buy: ").lower().strip()
    producto = next((p for p in productos if p["name"].lower() == nombre_producto), None)
    
    if not producto:
        print("Product not found")
        return
    
    while True:
        try:
            cantidad = int(input("Quantity: "))
            if cantidad <= 0:
                print("Quantity must be greater than 0")
                continue
            break
        except ValueError:
            print("Only numbers please")
    
    if cantidad > producto["stock"]:
        print(f"Insufficient stock! Available: {producto['stock']}")
        return
    
    descuentos = {"regular": 0, "vip": 10, "wholesale": 15}
    descuento = descuentos[tipo_cliente]
    
    subtotal = producto["unit_price"] * cantidad
    total = subtotal - (subtotal * descuento / 100)
    fecha = datetime.now().strftime("%Y-%m-%d")
    
    print("\n=== Sale summary ===")
    print(f"Customer: {cliente}")
    print(f"Type: {tipo_cliente} (discount: {descuento}%)")
    print(f"Product: {nombre_producto}")
    print(f"Quantity: {cantidad}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${subtotal * descuento / 100:.2f}")
    print(f"Total: ${total:.2f}")
    
    if input("\nConfirm sale? (Y/N): ").upper() == "Y":
        producto["stock"] -= cantidad
        from inventario import guardar_productos
        guardar_productos("productos.csv", productos)
        
        nueva_venta = {
            "customer": cliente,
            "customer_type": tipo_cliente,
            "product": nombre_producto,
            "quantity": cantidad,
            "date": fecha,
            "discount": descuento,
            "total": total
        }
        ventas.append(nueva_venta)
        guardar_ventas("ventas.csv", ventas)
        print("\nSale completed successfully!")
    else:
        print("Sale cancelled")

# ==================== HISTORIAL DE VENTAS ====================

def mostrar_ventas(ventas):
    """Mostrar todas las ventas registradas"""
    if not ventas:
        print("No sales registered")
        return
    print("\n=== Sales history ===")
    for i, v in enumerate(ventas, 1):
        print(f"{i}. {v['customer']} | {v['customer_type']} | {v['product']} x{v['quantity']} | "
              f"date: {v['date']} | discount: {v['discount']}% | total: ${v['total']:.2f}")

# ==================== REPORTES ====================

def mejores_productos(ventas):
    """Top 3 productos más vendidos"""
    if not ventas:
        print("No sales data")
        return
    conteo = {}
    for v in ventas:
        conteo[v["product"]] = conteo.get(v["product"], 0) + v["quantity"]
    top = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]
    print("\n=== Top 3 products ===")
    for i, (prod, cant) in enumerate(top, 1):
        print(f"{i}. {prod}: {cant} units sold")

def ventas_por_marca(ventas, productos):
    """Agrupar ventas por marca"""
    if not ventas:
        print("No sales data")
        return
    marcas = {p["name"]: p["brand"] for p in productos}
    agrupado = {}
    for v in ventas:
        marca = marcas.get(v["product"], "unknown")
        agrupado[marca] = agrupado.get(marca, 0) + v["total"]
    print("\n=== Sales by brand ===")
    for marca, total in agrupado.items():
        print(f"{marca}: ${total:.2f}")

def reporte_ingresos(ventas):
    """Calcular ingresos brutos y netos"""
    if not ventas:
        print("No sales data")
        return
    neto = sum(v["total"] for v in ventas)
    bruto = sum(map(lambda v: v["total"] / (1 - v["discount"]/100), ventas))
    print("\n=== Revenue report ===")
    print(f"Gross revenue: ${bruto:.2f}")
    print(f"Net revenue: ${neto:.2f}")
    print(f"Discounts applied: ${bruto - neto:.2f}")

def rendimiento_inventario(productos, ventas):
    """Evaluar rendimiento del inventario"""
    if not productos:
        print("No products")
        return
    vendidos = {}
    for v in ventas:
        vendidos[v["product"]] = vendidos.get(v["product"], 0) + v["quantity"]
    print("\n=== Inventory performance ===")
    for p in productos:
        s = vendidos.get(p["name"], 0)
        print(f"{p['name']}: stock {p['stock']} | sold {s} units")
