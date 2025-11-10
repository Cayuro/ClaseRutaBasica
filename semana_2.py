'''# Definición de funciones
def retornar_nota(estudiante):
    return estudiante[3]

lista_estudiantes = [
    ('Edward', 4.2,'Inglés', 3.8,'Matematicas'),
    ('Pepe', 2.5,'Inglés', 4.1,'Matematicas' ),
    ('Maria', 3.1,'Inglés',4.6 ,'Matematicas'),
    ('Carlos', 4.5,'Inglés', 2.9,'Matematicas'),
    ('Juanito',4.9,'Inglés', 4.6,'Matematicas'),
    ('Pedro', 3.6,'Inglés', 3.0,'Matematicas')
]

lista_ordenada = sorted(lista_estudiantes, key=retornar_nota, reverse=True)
print(lista_ordenada)

    #SIMPLIFICADO CON LAMBDA
def retornar_nota(estudiante):
    return estudiante[3]

lista_estudiantes = [
    ('Edward', 4.2,'Inglés', 3.8,'Matematicas'),
    ('Pepe', 2.5,'Inglés', 4.1,'Matematicas' ),
    ('Maria', 3.1,'Inglés',4.6 ,'Matematicas'),
    ('Carlos', 4.5,'Inglés', 2.9,'Matematicas'),
    ('Juanito',4.9,'Inglés', 4.6,'Matematicas'),
    ('Pedro', 3.6,'Inglés', 3.0,'Matematicas')
]

lista_ordenada = sorted(lista_estudiantes, key=lambda estudiante: estudiante[3], reverse=True)
print(lista_ordenada)
'''
'''
 #Definición de funciones *args y *kwargs
def enviar_mensaje(destinatario, asunto="(sin asunto)", *adjuntos, **metadatos):
    print(f"Para: {destinatario} | Asunto: {asunto}")
    
    if adjuntos:
        print("Adjuntos:", ", ".join(adjuntos))
    
    if metadatos:
        print("Meta:", metadatos)


# Ejemplos de uso
enviar_mensaje("coder@example.com")
enviar_mensaje("coder@example.com", "Bienvenida", "cv.pdf", "foto.png", prioridad="alta", etiqueta="onboarding")
'''
'''
    #DEFINICIÓN DE FUNCIONES MULTIPLES
def min_max(promedios):
    return min(promedios), max(promedios)

mn, mx= min_max([5, 4, 1, 3, 16, 21, 0])
print(f"El minimo es {mn} y el máximo {mx}")

    #CLOSURE - FUNCION DENTRO DE FUNCIÓN
    #Elevación al número x que defina en potencia
def potencia(n):
    def elevar(x):
        return x**n
    return elevar

eleva_2=potencia(2)
eleva_3=potencia(3)
eleva_4=potencia(4)

print(eleva_2(3), eleva_3(5), eleva_4(2))

    #Multiplicación por un número decidido
def crear_multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

por_3 = crear_multiplicador(3)
por_5 = crear_multiplicador(5)
por_8 = crear_multiplicador(8)

print(por_3(10), por_3(13), por_5(16),por_5(10), por_8(12), por_8(5), por_8(9))

    #Contador CLOSURE - cada contador es independiente
def crear_contador():
    count = 0
    def incrementar():
        nonlocal count
        count += 1
        return count
    return incrementar

contador_a = crear_contador()
contador_b = crear_contador()

print(contador_a(),contador_a(), contador_a(), contador_b(), contador_a(), contador_b(),contador_a(), contador_a(), contador_b(), "  ", contador_a)
print()

'''
'''
    #Closure operaciones, creando funciones para la calculadora
def operacion(operador):
    def operacion(x, y):
        if operador == '+':
            return x + y
        elif operador == '-':
            return x - y
        elif operador == '*':
            return x * y
        elif operador == '/':
            return x / y
        else:
            return None
    return operacion

sumar = operacion('+')
restar = operacion('-')
multiplicar = operacion('*')

print(sumar(10, 5),restar(10, 5),multiplicar(10, 5))
    
    #Closure para otras cosa
def generador_de_frases(persona):
    frases = []

    def agregar_frase(texto):
        frases.append(f"{persona} dice: {texto}")
        return frases[-1]
    
    def obtener_historial():
        return frases
    
    return agregar_frase, obtener_historial


hablar, historial = generador_de_frases("Einstein")

print(hablar("La imaginación es más importante que el conocimiento."))
print(hablar("La locura es hacer lo mismo esperando resultados distintos."))

print(historial())
'''

'''
coders = {
    "Pedro": {
        "apellido": "Doe",
        "edad": 30,
        "direccion": "123 Main St",
        "estado": True,
        "email": "john.doe@example.com"
    },
    "María José": {
        "apellido": "Garcia",
        "edad": 24,
        "direccion": "45 B Elm Rd",
        "estado": True,
        "email": "maria.garcia@example.com"
    },
    "Carolina": {
        "apellido": "Velez",
        "edad": 35,
        "direccion": "789 Oak Ave",
        "estado": False, # Ejemplo de un coder inactivo
        "email": "carlos.velez@example.com"
    },
    "Min": {
        "apellido": "Chen",
        "edad": 28,
        "direccion": "10 Pine Ln",
        "estado": True,
        "email": "laura.chen@example.com"
    }
}
print(coders["Pedro"]["direccion"], coders["Min"]["direccion"], coders["Carolina"]["direccion"])
print(coders.keys())
print(coders.items["Pedro"])
'''

'''    #Ejercicio 30 Agenda de contactos (lista de diccionarios)
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
'''
contact= {}

while True:
    opt= int(input("Ingrese la opción que decide: 1- ingresar contacto   2- ver contactos  3-salir: "))
    match opt:
        case 1:
            nombre= input("Agrege su nombre: ")
            city= input("Ingrese su ciudad: ")
            celular= int(input("Ingrese su numero de celular: "))
            contact[nombre]={'City':city, 'Telefono': celular}
        case 2:
            print("Tu lista de contactos quedó de la siguiente manera")
            for nombre, elements in contact.items():
                print(f"Nombre: {nombre}, numero: {celular}, Ciudad: {city}")
        case 3:
            break