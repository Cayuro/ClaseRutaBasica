from servicio import *
from archivo_csv import guardar_csv, cargar_csv, cargar_fusionar

ARCHIVO_CSV= "Inventario.csv"
inventario= cargar_csv(ARCHIVO_CSV)

def Menu():
    global inventario
    while True:
        opcion = input(
            "1. Agregar\n2. Mostrar\n3. Buscar\n4. Actualizar\n5. Eliminar\n6. Estadísticas\n7. Guardar CSV\n8. Cargar CSV\n9. Salir\nElige: "
        )
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            encontrados = buscar_producto(inventario, nombre)
            for p in encontrados:
                print(p)
        elif opcion == "4":
            actualizar_producto(inventario)
        elif opcion == "5":
            nombre = input("Nombre a eliminar: ")
            eliminar_producto(inventario, nombre)
        elif opcion == "6":
            stats = calcular_estadisticas(inventario)
            print(stats)
        elif opcion == "7":  # Guardar CSV
            guardar_csv(inventario, ARCHIVO_CSV)

        elif opcion == "8":  # Cargar CSV
            cargar_fusionar(inventario, ARCHIVO_CSV)
            
        elif opcion == "9":
            print("Eso fue todo por hoy, un placer")
            break
        else:
            print("Opción inválida")

Menu()
