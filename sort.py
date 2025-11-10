'''
def particion(Arreglo, inicio, fin):
    # Tarea: Seleccionar el pivote (último elemento del sub-arreglo)
    pivote = Arreglo[fin]
    
    # Índice del elemento más pequeño, e indica la posición correcta del pivote encontrado hasta ahora
    i = inicio - 1
    
    # Recorrer todos los elementos desde 'inicio' hasta 'fin-1'
    for j in range(inicio, fin):
        # Si el elemento actual es menor o igual al pivote
        if Arreglo[j] <= pivote:
            # Incrementar el índice del elemento más pequeño
            i = i + 1
            # Intercambiar Arreglo[i] y Arreglo[j]
            Arreglo[i], Arreglo[j] = Arreglo[j], Arreglo[i]
            
    # Intercambiar el pivote (Arreglo[fin]) con el elemento en la posición i + 1
    Arreglo[i + 1], Arreglo[fin] = Arreglo[fin], Arreglo[i + 1]
    
    # Devolver el índice de la partición
    return i + 1
'''


'''
def quicksort(Arreglo, inicio, fin):
    # La condición de parada es que el índice 'inicio' no sea mayor o igual al índice 'fin'
    if inicio < fin:
        
        # Obtener el índice del pivote, donde el arreglo está dividido
        indice_pivote = particion(Arreglo, inicio, fin)
        
        # Llamada recursiva para ordenar los elementos ANTES del pivote
        quicksort(Arreglo, inicio, indice_pivote - 1)
        
        # Llamada recursiva para ordenar los elementos DESPUÉS del pivote
        quicksort(Arreglo, indice_pivote + 1, fin)
'''


'''
# TOMA DE DATOS ORIGINAL
Arreglo = []
n = int(input("Ingrese el numero de elementos: "))

for i in range(n):
    num = int(input(f"Ingrese el número en la posición {i+1}: "))
    Arreglo.append(num)

# --- IMPLEMENTACIÓN DE QUICKSORT ---

# [Insertar aquí la definición de la función particion]
# [Insertar aquí la definición de la función quicksort]

# --- LLAMADA A LA FUNCIÓN ---

# Los límites son: inicio = 0 y fin = n-1 (el último índice del arreglo)
inicio = 0
fin = len(Arreglo) - 1

print("\nArreglo original:", Arreglo)

# Iniciar el proceso de ordenamiento
quicksort(Arreglo, inicio, fin)

print("Arreglo ordenado:", Arreglo)
'''