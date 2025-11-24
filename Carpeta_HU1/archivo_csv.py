import csv

def guardar_csv(inventario, ruta):
    """Guarda el inventario en CSV de forma simple."""
    if not inventario:
        print("Inventario vacío. No se puede guardar.")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Inventario guardado en: {ruta}")

    except Exception as e:
        print(f"Error guardando CSV: {e}")


def cargar_csv(ruta):
    """Carga CSV y retorna inventario como lista de diccionarios."""
    inventario = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames != ["nombre", "precio", "cantidad"]:
                print("Error: encabezado CSV inválido.")
                return []

            for fila in reader:
                try:
                    inventario.append({
                        "nombre": fila["nombre"].strip(),
                        "precio": float(fila["precio"]),
                        "cantidad": int(fila["cantidad"])
                    })
                except:
                    errores += 1

        if errores:
            print(f"{errores} filas inválidas omitidas.")

        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado.")
        return []
    except Exception as e:
        print(f"Error cargando CSV: {e}")
        return []

def cargar_fusionar(inventario, archivo):
    cargados = cargar_csv(archivo)
    if not cargados:
        print("No se cargó nada.")
        return inventario
    decision = input("Deseas sobreescribir el inventario, (1) si, (2) no : ").strip().upper()
    if decision == "S":
        print("Inventario sobrescrito.")
        return cargados
    # Si NO sobrescribe → fusionar
    print("Fusionando inventarios...")
    # Crear mapa para búsqueda rápida
    mapa = {p["nombre"].lower(): p for p in inventario}
    for nuevo in cargados:
        nombre = nuevo["nombre"].lower()
        if nombre in mapa:
            mapa[nombre]["cantidad"] += nuevo["cantidad"]
            mapa[nombre]["precio"] = nuevo["precio"]
        else:
            inventario.append(nuevo)
    print("Inventarios fusionados correctamente.")
    return inventario