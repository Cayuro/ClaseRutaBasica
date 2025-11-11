option=0
value=0
inventary={}
print("This is your agenda: \n1- add product  \n2- print product  \n3- Calculate stadistics  \n4- out\n")
while option!=4:
    try: 
        option= int(input("1- Add  2- Show  3- Calculate  4- out\n"))
    except ValueError:
        print("Error, this option isn't correct")
        continue

    if option == 1:
        name= input("insert the name: ")
        try:
            price= int(input("insert the price: "))
            quantity= int(input("insert the quantity: "))
        except ValueError:
            print("the price should be a number")
            continue

        inventary[name]={'Price': price, 'Quantity': quantity}

    elif option == 2:
        for name,element in inventary.items():
            print(inventary)

    elif option == 3:
        for name,elements in inventary.items():
            value+= inventary[name]['Price']*inventary[name]['Quantity']
            print(f"You buy {inventary[name]['Quantity']} each one for {inventary[name]['Price']} ")
            
        print(f"The total value is {value}")
    #Esto es todo por hoy
