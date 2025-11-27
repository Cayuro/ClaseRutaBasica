from datetime import datetime
from file_csv import save_sales

library= "library.csv"

# ==================== REGISTRAR UNA VENTA ====================

def client_type(): # Válida si el ID está bien
    while True:
        option = input("Select type (1-3): ").strip()
        if option in ["1", "2", "3"]:
            break
        print("Invalid option, choose 1, 2 or 3")
    
    types = {"1": "regular", "2": "vip", "3": "wholesale"}
    customer_type = types[option]
    return customer_type

def register_sale(library, sales): # Registrar una nueva venta con validaciones básicas
    
    client = input("Customer name: ").title().strip()
    
    customer_type= client_type()
    
    if not library:
        print("No products available")
        return
    
    print("\nAvailable products:")
    amarillo = '\033[33m'
    verde = '\033[32m'
    cierre= '\033[0m'
    for p in library:
        print(f"{p['Title']:<24} | {p['Author']:<26} | {p['Category']:<16} | {amarillo}{p['Price']:<6} | {verde}{p['Quantity']:<6}{cierre}")
    
    book_name = input("\nProduct name to buy: ").title().strip()
    book = next((p for p in library if p["Title"].title() == book_name), None)
    
    if not book:
        print("Product not found")
        return
    
    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than 0")
                continue
            break
        except ValueError:
            print("Only numbers please")
    
    if quantity > book["Quantity"]:
        print(f"Insufficient stock! Available: {book['Quantity']}")
        return
    
    discounts = {"regular": 0, "vip": 10, "wholesale": 15}
    discount = discounts[customer_type]
    
    subtotal = book["Price"] * quantity
    total = subtotal - (subtotal * discount / 100)
    date = datetime.now().strftime("%Y-%m-%d")
    
    print("\n=== Sale summary ===")
    print(f"Customer: {client}")
    print(f"Type: {customer_type} (discount: {discount}%)")
    print(f"Product: {book_name}")
    print(f"Quantity: {quantity}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${subtotal * discount / 100:.2f}")
    print(f"Total: ${total:.2f}")
    
    if input("\nConfirm sale? (Y/N): ").upper() == "Y":
        book["Quantity"] -= quantity
        from inventory import save_product
        save_product("library.csv", library)
        
        new_sell= {
            "customer": client,
            "customer_type": customer_type,
            "product": book_name,
            "quantity": quantity,
            "date": date,
            "discount": discount,
            "total": total
        }
        sales.append(new_sell)
        save_sales("sales.csv", sales)
        print("\nSale completed successfully!")
    else:
        print("Sale cancelled")


# ==================== HISTORIAL DE sales ====================

def show_sales(sales):
    """Mostrar todas las sales registradas"""
    if not sales:
        print("No sales registered")
        return
    print("\n=== Sales history ===")
    for i, v in enumerate(sales, 1):
        print(f"{i}. {v['customer']} | {v['customer_type']} | {v['product']} x{v['quantity']} | "
            f"date: {v['date']} | discount: {v['discount']}% | total: ${v['total']:.2f}")


# ==================== REPORTES ====================

def bestsellers(sales):
    """Top 3 Libros más vendidos"""
    if not sales:
        print("No sales data")
        return
    count = {}
    for v in sales:
        count[v["product"]] = count.get(v["product"], 0) + v["quantity"]
    top = sorted(count.items(), key=lambda x: x[1], reverse=True)[:3]
    print("\n=== Top 3 products ===")
    for i, (prod, cant) in enumerate(top, 1):
        print(f"{i}. {prod}: {cant} units sold")

def brand_sales(sales, library):
    """Agrupar sales por Author"""
    if not sales:
        print("No sales data")
        return
    authors = {p["Title"].title(): p["Author"] for p in library}
    agrupado = {}
    for v in sales:
        author = authors.get(v["product"].title(), "unknown")
        agrupado[author] = agrupado.get(author, 0) + v["total"]
    print("\n=== Sales by Author ===")
    for author, total in agrupado.items():
        print(f"{author}: ${total:.2f}")

def income_report(sales):
    """Calcular ingresos brutos y netos"""
    if not sales:
        print("No sales data")
        return
    neto = sum(v["total"] for v in sales)
    bruto = sum(map(lambda v: v["total"] / (1 - v["discount"]/100), sales))
    print("\n=== Revenue report ===")
    print(f"Gross revenue: ${bruto:.2f}")
    print(f"Net revenue: ${neto:.2f}")
    print(f"Discounts applied: ${bruto - neto:.2f}")

def inventory_performance(library, sales):
    """Evaluar rendimiento del inventario"""
    if not library:
        print("No products")
        return
    vendidos = {}
    for v in sales:
        vendidos[v["product"]] = vendidos.get(v["product"], 0) + v["quantity"]
    print("\n=== Inventory performance ===")
    for p in library:
        s = vendidos.get(p["Title"], 0)
        print(f"{p['Title']}: stock {p['Quantity']} | sold {s} units")
        
