from file_csv import save_product, download_products

library_csv = "library.csv"                         # iniciamos la librería por fuera para evitar errores
library = []                                        # iniciamos vacia la librería
def validator_text(msg):                            # PRUEBA DEJANDO POR FUERA TODO LO QUE NO SEA TEXTO
        while True:
            valid= input(msg).title().strip()                
            if any(character.isdigit() for character in valid):
                print("Take care, only letters allowed")
                continue
            elif not valid:
                print("My brother you are stupid or what, enter anything please")
                continue
            return valid

def validator_float(msg):                           #DEJANDO POR FUERA LO QUE NO SEAN NUMEROS
    while True:
            try:
                value= float(input(msg))
                return value
            except ValueError:
                print("Take care, only float numbers allowed")

def validator_int(msg):                             # ASEGURA QUE LO QUE HAYA EN CANTIDAD SEA UN VALOR ENTERO
    while True:
            try:
                value= int(input(msg))
                return value
            except ValueError:
                print("Take care, only numbers allowed, without dot, (not floats allowed)")

def register_product(library):                      #AQUPÍ REGISTRAMOS EL INVENTARIO Y VAMOS llamando las funciones para validar que sea valido
    title = validator_text("what is the name of the book? ")
    author = validator_text("who is the author? ")
    category = validator_text("define the category? ")
    price = validator_float("price of the book: ")
    quantity= validator_int("what amount of books are there? ")
    print(f"You have the next: {title} | {author} | {category} | {price} | {quantity}") #SE IMPRIME MÁS O MENOS CÓMO VA A QUEDAR
    if input("The information is correct, add the new book? (Y/N)").lower() == 'y':     
        library.append({"Title": title, "Author": author, "Category": category, "Price": price, "Quantity": quantity})

        save_product(library_csv,library)               #AQUÍ SE GUARDAN LOS REGISTROS EN EL INVENTARIO
    else:
        print("You have cancelled the register") 

def show_products(library):
    if not library:                                     #CONFIRMA QUE EXISTA LA LIBRERÍA (ARCHIVO.CSV)
        print("You don't have books to add")
        return
    print("="*8+" BOOKSELF "+"="*8)
    amarillo = '\033[33m'
    verde = '\033[32m'
    cierre= '\033[0m'
    for p in library:                                   #SE ITERA DENTRO DE LA LISTA, PARA IMPRIMIRLA COMPLETA.
        print(f"{p['Title']:<24} | {p['Author']:<26} | {p['Category']:<16} | {amarillo}{p['Price']:<6} | {verde}{p['Quantity']:<6}{cierre}") 

def update_product(library):                            #VAMOS A ENTRAR A HACER UPDATE, INGRESAMOS A LOS VALORES POR MEDIO DE LA CLAVE
    name= input("Name the title that you wanna update: ").title().strip()
    for p in library:                                   #  ITERAMOS PARA QUE P VAYA TOMANDO EL VALOR DE CADA ELEMENTO
        if name in p["Title"].title():                  #VALIDAMOS SI EL NOMBRE QUE NOS DIERON SE PARECE A ALGÚN NOMBRE
            print(f"Here is the title: {p['Title']} | {p['Author']} | {p['Category']} | {p['Price']} | {p['Quantity']}")
            change = input("What do u want to correct? (1,2,3,4,5) \n1-Title 2-Author 3-Category 4-Price 5-Quantity: ")
            if change == '1':                           # PRUEBA HACIENDO VALIDACIONES PARA QUE PUEDA CAMBIAR DE A 1 COSA
                new_title = validator_text("what is the name of the book? ")
                p["Title"] = new_title
            elif change == '2':
                new_author = validator_text("Enter the correct author: ")
                p["Author"] = new_author
            elif change == '3':
                new_category = validator_text("Enter the new category: ")
                p["Category"] =  new_category
            elif change == '4':
                new_price= validator_float("Enter the new price: ")
                p["Price"] =  new_price
            elif change == '5':
                new_quantity= validator_int("Enter the new price: ")
                p["Quantity"] = new_quantity
            else:
                print("Enter a valid option\n1-Title 2-Author 3-Category 4-Price 5-Quantity")

            save_product("library.csv",library)         # Aquí debe hacer el guardado de la librería tal y como queda despues del update
            print(f"Here is the correct log: {p['Title']} | {p['Author']} | {p['Category']} | {p['Price']} | {p['Quantity']}")
            return
    print("Here aren't books with a similar name, try again")
    
def delete_product(library):                            #ELIMINAR ALGÚN REGISTRO, SE DEJA UN CONTADOR POR SI HAY VARIOS QUE COINCIDEN
    count=0                                              
    name = input("What Book do u want to delete: ").title().strip()
    for p in library:
        print(f"Here is the title: {p['Title']} | {p['Author']} | {p['Category']} | {p['Price']} | {p['Quantity']}")
        if name in p["Title"].title():                  #ESTE CONDICIONAL PERMITE QUE HAYAN VARIAS COINCIDENCIAS
            if input(f"Are you sure, you want to delete {count} books (Yes/Not)").upper() in "Yes":
                library.remove(p)                       #AQUÍ ELIMINAMOS EL REGISTRO
                save_product("library.csv", library)    #SE GUARDA LA INFORMACIÓN 
                print("Product deleted")
            else:
                print("Cancelled")
            return
        count+= 1

    print("Book not found")

def preloaded_books(library_csv="library.csv"):         # SE HACE UN PRECARGADO, PARA QUE CUANDO NO SE ENCUENTREN REGISTROS TENGA ESTOS 5 POR DEFECTO

    library = download_products("library.csv")          #SE CARGA LO QUE CONTIENE EL ARCHIVO BIBLIOTECA (LIBRARY) PARA VER SI TIENE DATOS
    # Precargar si no hay libros
    if not library:
        library= [{"Title": "El principito", "Author": "Antoine Saint Exupery", "Category": "Drama", "Price": 43, "Quantity": 34},
            {"Title": "La oculta", "Author": "Hector Abad Faciolince", "Category": "Novela", "Price": 700, "Quantity": 12},
            {"Title": "Una habitacion propia", "Author": "Virginia Wolf", "Category": "Empoderamiento", "Price": 800, "Quantity": 25},
            {"Title": "Cien Años de soledad", "Author": "Gabriel Garcia Marquez", "Category": "Ficcion", "Price": 1000, "Quantity": 17},
            {"Title": "El Olvido que seremos", "Author": "Hector Abada Faciolince", "Category": "Novela", "Price": 23, "Quantity": 23}]
        
        save_product(library_csv, library)
        print("5 Books were preloaded")
    
    return library