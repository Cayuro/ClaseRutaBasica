# main.py
# Orchestrator: menus in English, loads/saves CSV, catches exceptions.

from io_csv import (INV_HEADERS, SALE_HEADERS, ensure_file,
                    load_inventory_csv, save_inventory_csv,
                    load_sales_csv, save_sales_csv)
from inventory_loaded import default_inventory_rows
from invetory import list_products, add_product, update_product, delete_product
from sales import register_sale, list_sales
from reports import top3_products, sales_by_brand, income_totals, inventory_performance
from ui import (print_inventory, print_sales, print_brand_report, print_inventory_perf)

INV_PATH = "inventory.csv"
SALES_PATH = "sales.csv"

def bootstrap():
    ensure_file(INV_PATH, default_inventory_rows())
    ensure_file(SALES_PATH, [SALE_HEADERS])

def inventory_menu(inv: dict):
    while True:
        print("\n--- Inventory Menu ---")
        print("1. Add a product")
        print("2. Update a product")
        print("3. Delete a product")
        print("4. View all products")
        print("5. Save inventory to CSV")
        print("6. Go back")
        op = input("Choose an option: ").strip()
        if op == "1":
            name = input("Product name: "); brand = input("Brand: ")
            category = input("Category: "); price = input("Unit price: ")
            stock = input("Stock: "); warranty = input("Warranty (months): ")
            pid, msg = add_product(inv, name, brand, category, price, stock, warranty)
            print(f"{msg}. ID: {pid}" if pid != -1 else msg)
        elif op == "2":
            try:
                pid = int(input("Product ID: "))
            except Exception:
                print("Invalid ID"); continue
            print("Leave empty to skip a field.")
            updates = {
                "name": input("Name: "),
                "brand": input("Brand: "),
                "category": input("Category: "),
                "price": input("Price: "),
                "stock": input("Stock: "),
                "warranty": input("Warranty: "),
            }
            print(update_product(inv, pid, updates))
        elif op == "3":
            try:
                pid = int(input("Product ID: "))
            except Exception:
                print("Invalid ID"); continue
            print(delete_product(inv, pid))
        elif op == "4":
            print_inventory(list_products(inv))
        elif op == "5":
            save_inventory_csv(INV_PATH, inv); print("Inventory saved.")
        elif op == "6":
            break
        else:
            print("Invalid option.")

def reports_menu(inv: dict, sales: list):
    while True:
        print("\n--- Reports Menu ---")
        print("1. Top 3 best-selling products")
        print("2. Sales grouped by brand")
        print("3. Gross and net income")
        print("4. Inventory performance")
        print("5. View sales history")
        print("6. Go back")
        op = input("Choose an option: ").strip()
        if op == "1":
            top = top3_products(sales)
            if not top: print("No sales data.")
            else:
                for i, (n, q) in enumerate(top, 1): print(f"{i}. {n} - {q} units")
        elif op == "2":
            print_brand_report(sales_by_brand(sales))
        elif op == "3":
            t = income_totals(sales)
            print(f"Total gross: ${t['gross']:.2f} | Discounts: ${t['discounts']:.2f} | Net: ${t['net']:.2f}")
        elif op == "4":
            print_inventory_perf(inventory_performance(inv, sales))
        elif op == "5":
            print_sales(list_sales(sales))
        elif op == "6":
            break
        else:
            print("Invalid option.")

def main_menu(inv: dict, sales: list):
    while True:
        print("\n===== ELECTRONICS STORE SYSTEM =====")
        print("1. Manage inventory")
        print("2. Register a sale")
        print("3. View sales reports")
        print("4. Save all data")
        print("5. Reload from CSV")
        print("6. Exit")
        op = input("Enter an option: ").strip()
        if op == "1":
            inventory_menu(inv)
        elif op == "2":
            customer = input("Customer name: ")
            ctype = input("Customer type (regular/VIP/wholesale): ")
            pid = input("Product ID: "); qty = input("Quantity: ")
            _, msg = register_sale(inv, sales, customer, ctype, pid, qty)
            print(msg)
        elif op == "3":
            reports_menu(inv, sales)
        elif op == "4":
            save_inventory_csv(INV_PATH, inv)
            save_sales_csv(SALES_PATH, sales)
            print("Data saved to CSV.")
        elif op == "5":
            inv.clear(); inv.update(load_inventory_csv(INV_PATH))
            sales.clear(); sales.extend(load_sales_csv(SALES_PATH))
            print("Data reloaded from CSV.")
        elif op == "6":
            print("Exiting system. Goodbye."); break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    try:
        bootstrap()
        inventory = load_inventory_csv(INV_PATH)
        sales = load_sales_csv(SALES_PATH)
        main_menu(inventory, sales)
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting gracefully.")
