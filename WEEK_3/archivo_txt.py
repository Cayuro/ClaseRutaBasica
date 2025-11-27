def crear_archivo(nombre):
    with open(nombre, "w") as file:
        file.write("Archivo creado")
        return f"Archivo {nombre} creado correctamente"
    
def agregar_linea(nombre, text):
    with open(nombre,"a") as file:
        file.write(text)
        return f"Se agrego la linea {text} al archivo {nombre}"
    
def leer_archivos(nombre):
    with open(nombre, "r") as file:
        return file.read()

print("el mejor")