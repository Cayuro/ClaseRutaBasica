    #Ejercicio 28 Gestor de estudiantes (mini base de datos)
Estudiantes = {}
while True:
    print("\nGestor de Estudiantes\n1. Agregar estudiante\n2. Ver estudiantes\n3. Salir")
    opcion = int(input("Seleccione una opción (1-3): "))
    
    match opcion:
    case 1:
        name = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        calificacion = input("Ingrese la calificación del estudiante: ")
        Estudiantes[name] = {'Edad': edad, 'Calificación': calificacion} #crea un diccionario dentro de otro diccionario
        print(f"Estudiante {name} agregado.") 
    case 2:
        if not Estudiantes:
            print("No hay estudiantes registrados.") #verifica si el diccionario está vacío
        else:
            print("\nLista de Estudiantes:")
            for name, info in Estudiantes.items():
                print(f"Nombre: {name}, Edad: {info['Edad']}, Calificación: {info['Calificación']}")
    case 3:
        print("Saliendo del gestor de estudiantes. ¡Hasta luego!")
        break
    case _:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 3.")