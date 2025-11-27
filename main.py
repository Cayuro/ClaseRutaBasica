from file_csv import download_sales
from inventory import show_products, register_product, update_product, delete_product, preloaded_books
from sales import register_sale, show_sales, bestsellers, brand_sales, income_report, inventory_performance

library_csv= "library.csv"
library=[]
option=0
def menu():
    # Cargar datos iniciales
    sales = download_sales("sales.csv")         #SE CARGAN LOS DATOS DE VENTAS
    library = preloaded_books()                 #SE CARGAN LOS DATOS DE BIBLIOTECA
    
    while True:
        print("\n" + "="*42 + "\n WELCOME TO THE LIBRARY "+ "\n" +"-"*42 + '''
[INVENTORY]:    1. Add book 
                2. View book
                3. Update Book
                4. Delete Book
[SALES]         5. Register sale
                6. View sales history
[REPORTS]       7. Top 3 book
                8. Sales by author
                9. Income report
               10. Inventory performance
[SYSTEM]       11. Exit''' + "\n" + "="*42)
        
        option = input("Choose an option: ")
        #LLAMAMOS CADA UNA DE LAS FUNCIONES PREVIAMENTE CREADAS
        if option == '1': register_product(library)                 # ESTAS SON DE INVENTORY
        elif option == '2': show_products(library)                  # todo esto lo revisamos en inventory.py
        elif option == '3': update_product(library)                 #    
        elif option == '4': delete_product(library)                 #    
        elif option == '5': register_sale(library, sales)           # HACIA ABAJO FUNCIONES DE VENTAS            
        elif option == '6': show_sales(sales)                       # todo esto en sales.py 
        elif option == '7': bestsellers(sales)                      # 
        elif option == '8': brand_sales(sales, library)             #
        elif option == '9': income_report(sales)                    #
        elif option == '10': inventory_performance(library, sales)  #
        elif option == '11':
            print("System closed. Goodbye!")
            break
        else:
            print("Invalid option")


menu()