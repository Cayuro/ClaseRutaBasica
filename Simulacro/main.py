
from inventario import guardar_productos, cargar_productos, agregar_producto, ver_productos, actualizar_producto, eliminar_producto
from ventas import cargar_ventas, registrar_venta, mostrar_ventas, mejores_productos, ventas_por_marca, reporte_ingresos, rendimiento_inventario

def menu():
    # Cargar datos iniciales
    productos = cargar_productos("productos.csv")
    ventas = cargar_ventas("ventas.csv")
    
    # Precargar si no hay productos
    if not productos:
        productos = [
            {"name": "headphones", "brand": "sony", "category": "audio", "unit_price": 43, "stock": 34, "warranty": 6},
            {"name": "smartphone", "brand": "nokia", "category": "phones", "unit_price": 700, "stock": 12, "warranty": 18},
            {"name": "smartwatch", "brand": "hwawei", "category": "wearables", "unit_price": 800, "stock": 25, "warranty": 24},
            {"name": "laptop", "brand": "HP", "category": "computers", "unit_price": 1000, "stock": 17, "warranty": 12},
            {"name": "USB", "brand": "DELL", "category": "USB", "unit_price": 23, "stock": 23, "warranty": 24}
        ]
        guardar_productos("productos.csv", productos)
        print("5 products were preloaded")
    
    while True:
        print("\n" + "="*38)
        print("   ELECTRONIC STORE MANAGEMENT SYSTEM")
        print("-"*38)
        print(" [INVENTORY]")
        print(" 1. Add product")
        print(" 2. View products")
        print(" 3. Update product")
        print(" 4. Delete product")
        print(" [SALES]")
        print(" 5. Register sale")
        print(" 6. View sales history")
        print(" [REPORTS]")
        print(" 7. Top 3 products")
        print(" 8. Sales by brand")
        print(" 9. Revenue report")
        print(" 10. Inventory performance")
        print(" [SYSTEM]")
        print(" 11. Exit")
        print("="*38)
        
        try:
            opcion = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a number")
            continue
        
        if opcion == 1: agregar_producto(productos)
        elif opcion == 2: ver_productos(productos)
        elif opcion == 3: actualizar_producto(productos)
        elif opcion == 4: eliminar_producto(productos)
        elif opcion == 5: registrar_venta(productos, ventas)
        elif opcion == 6: mostrar_ventas(ventas)
        elif opcion == 7: mejores_productos(ventas)
        elif opcion == 8: ventas_por_marca(ventas, productos)
        elif opcion == 9: reporte_ingresos(ventas)
        elif opcion == 10: rendimiento_inventario(productos, ventas)
        elif opcion == 11:
            print("System closed. Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    menu()
