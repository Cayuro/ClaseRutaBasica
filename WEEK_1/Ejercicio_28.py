    #Ejercicio 28 Gestor de estudiantes (mini base de datos)
Estudiantes = {}
while True:
    print("\nGestor de Estudiantes\n1. Agregar estudiante\n2. Ver estudiantes\n3. Salir")
    opcion = int(input("Seleccione una opción (1-3): "))
    
    match opcion:
        case 1:
            name = input("Ingrese el nombre del estudiante: ")
            while True:
                try: #evita que la edad sea texto, o numeron o valido
                    edad = int(input("Ingrese la edad del estudiante: ")) 
                    if edad <= 5 or edad > 100: #limita la edad del estudiante entre 6 y 100 años
                        print("La edad deber ser un número entre 6 y 100")
                    break
                except ValueError:
                    print("La edad debe ser un número válido entre 6 y 100.")
            while True:
                try:
                    calificacion = int(input("Ingrese la calificación del estudiante: "))
                    if (calificacion < 0 or calificacion > 5):
                        raise ValueError("La calificación es inválida")
                    break
                except ValueError:
                    print("Calificaciones validas solo entre 0 y 5.")
                    
            Estudiantes[name] = {'Edad': edad, 'Calificación': calificacion} #crea un diccionario dentro de otro diccionario
            print(f"Estudiante {name} agregado.") 
        case 2:
            if not Estudiantes:
                print("No hay estudiantes registrados.") #verifica si el diccionario está vacío
            else:
                print("\nLista de Estudiantes:")
                for name, datos in Estudiantes.items(): # va mostrando en el diccionario estudiantes, y lo recorre por su clave nombre
                    print(f"Nombre: {name}, Edad: {datos['Edad']}, Calificación: {datos['Calificación']}") # la info es lo que se encuentra en el diccionario anidado.
        case 3:
            print("Saliendo del gestor de estudiantes. ¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 3.")