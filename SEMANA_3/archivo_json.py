import json

def guardar_json(nombre,data):
    with open(nombre, "w") as file:      # igual que en el otro, lo que cambia es por ejemplo que el indent=4 lo ordena
        json.dump(data, file, indent=None)  #Aqui le estamos especificando que vamos a trabajar con un archivo json
    #por ejemplo el None hace que no de sangría, todo dentro de la misma linea de código