import csv
#llamamos el archivo usuario.csv en modo lectura, lo leemos y abajo lo convertimos en lista

def downloading_csv(archivo):
    with open(archivo, "r") as file:
        reader = csv.DictReader(file)
        usuarios = list(reader)
    return usuarios

def validator_login(archivo):
    usuarios = downloading_csv(archivo)
    name = validator_name(archivo).lower()
    for e in usuarios:
        if name == e["User"].lower():
            password = input("Now the password: ")
            number_try= 0
            while number_try < 3:
                if password == e["Password"]:
                    print(f"WELCOME {name} THIS IS THE MENU")
                    return True
                elif number_try == 2:
                    print("YOU HAVE AN ERROR, WE ARE GOING OUT, BLOCKING THE ACCOUNT")
                    raise StopAsyncIteration
                elif number_try <2:
                    print("Try Again")
                    number_try += 1
                    password = input("Now the password: ")

def validator_name(archivo):
    usuarios = downloading_csv(archivo)
    number_try= 0
    while number_try < 5:
        user_name = input("Enter the username: ")
        user_coincidence = next((user for user in usuarios if user["User"].lower() == user_name.lower()),None)
        if user_coincidence:
            return user_name
        elif number_try == 4:
            print("A LOT OF TRIES OF LOG, WE ARE BLOCKING THE PAGE")
            raise StopIteration
        elif number_try < 4:
            print("It is not a valid user name")
            number_try +=1
         

def menu(archivo):
    if validator_login(archivo):
        print("""1. ADD A SOCCER TEAM
                 2. SHOW THE SOCCER TEAM
                 3. UPDATE A SOCCER TEAM
                 4. DELETE A SOCCER TEAM""")
        

menu("usuarios.csv")