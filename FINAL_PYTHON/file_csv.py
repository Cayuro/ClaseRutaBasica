import csv
import os

library_csv= "library.csv"
sales_csv= "sales.csv"
library = []

# ARCHIVO CSV PARA CARGAR LIBRERÍA

def save_product(library_csv, library):
    with open(library_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Author", "Category", "Price", "Quantity"])
        for p in library:
            writer.writerow([p["Title"], p["Author"], p["Category"], p["Price"], p["Quantity"]])
    print(f"Inventory saved in {library_csv}")

def download_products(library_csv):
    lista = []
    if not os.path.exists(library_csv):
        return lista
    with open(library_csv, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            title, author, category, price,quantity = row
            lista.append({"Title": title, "Author": author, "Category": category,
                        "Price": float(price), "Quantity": int(quantity)})
    return lista


#  ARCHIVO CSV PARA VENTAS 

def download_sales(sales_csv): #cargar ventas
    """Carga todas las ventas desde un archivo CSV"""
    lista = []
    if not os.path.exists(sales_csv):
        return lista
    
    with open(sales_csv, "r") as f:
        reader = csv.reader(f)
        next(reader)  # saltar encabezado
        for row in reader:
            customer,customer_type, book, quantity, date, discount, total = row
            lista.append({
                "customer": customer,
                "customer_type": customer_type,
                "product": book,
                "quantity": int(quantity),
                "date": date,
                "discount": float(discount),
                "total": float(total)
            })
    return lista

def save_sales(sales_csv, ventas):
    """Guarda todas las ventas en un archivo CSV"""
    with open(sales_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["customer", "customer_type", "product", "quantity", "date", "discount", "total"])
        for v in ventas:
            writer.writerow([v["customer"], v["customer_type"], v["product"],
                            v["quantity"], v["date"], v["discount"], v["total"]])
    print(f"Sales saved in {sales_csv}")