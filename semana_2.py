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
   
    #Closure operaciones, creando funciones para la calculadora
def fabrica_operacion(operador):
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

sumar = fabrica_operacion('+')
restar = fabrica_operacion('-')
multiplicar = fabrica_operacion('*')

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




