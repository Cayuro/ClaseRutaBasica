import csv

'''import csv

def agregar_encabezados(name, principal):
    with open(name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(principal)

principal= ["Nombre", "Tipo_Usuario", "Fecha", "Edad"]

print(agregar_encabezados("juan.csv", principal))'''

def crear_csv(nombre="juan.csv", principal=["Nombre","Edad"]):
    with open(nombre,"w", newline="") as file:
        escritor= csv.writer(file)
        escritor.writerow(principal)

def agregar_linea(nombre,datos):
    with open(nombre, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(datos)

        print("Semana 3")