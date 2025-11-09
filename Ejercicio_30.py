    #Ejercicio 30 Agenda de contactos (lista de diccionarios)
Contactos = {}
while True:
    print("\nGestor de Contactos\n1. Agregar Contacto\n2. Ver Contactos\n3. Salir")
    opcion = int(input("Seleccione una opción (1-3): "))
    
    match opcion:
        case 1:
            name = input("Ingrese el nombre del Contacto: ")
            while True:
                try: #evita que la numero sea texto, o numeron o valido
                    numero = int(input("Ingrese el numero del Contacto: ")) 
                    if numero < 1000000 or numero > 9999999999: #limita el numero para que esté entre 7 y 10 caracteres
                        raise ValueError("el numero deber ser un número entre 7 y 10 digitos") #lo envía al exccept
                    break
                except ValueError:
                    print("el numero debe ser un número válido, entre 7 y 10 digitos.")
            while True:
                try:
                    ciudad = input("Ingrese la Ciudad del Contacto: ")
                    if ciudad.isdigit(): #limita la ciudad a no ser numeros
                        raise ValueError("la Ciudad es inválida") #lo envía al except
                    break
                except ValueError:
                    print("lo numeros no son Ciudades.")
                    
            Contactos[name] = {'numero': numero, 'Ciudad': ciudad} #crea un diccionario dentro de otro diccionario
            print(f"Contacto {name} agregado.") 
        case 2:
            if not Contactos:
                print("No hay Contactos registrados.") #verifica si el diccionario está vacío
            else:
                print("\nLista de Contactos:")
                for name, datos in Contactos.items(): # va mostrando en el diccionario Contactos, y lo recorre por su clave nombre
                    print(f"Nombre: {name}, numero: {datos['numero']}, Ciudad: {datos['Ciudad']}") # la info es lo que se encuentra en el diccionario anidado.
        case 3:
            print("Saliendo del gestor de Contactos. ¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 3.")