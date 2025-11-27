from archivos_csv import crear_csv, agregar_linea
from archivo_json import guardar_json

print(crear_csv(principal=["Organización", "Empleado", "Rango"]))
print(agregar_linea("juan.csv", ["Blackbird", "Juan Esteban", "Coder"]))
print(agregar_linea("juan.csv", ["Textil", "Juan pablo", "Coder"]))
print(agregar_linea("juan.csv", ["Blackbird", "Alejandro", "TL"]))
print(agregar_linea("juan.csv", ["Sistecrédito", "Jhon", "Coder"]))
print(guardar_json("info.json",{"Curso": "python", "Nivel": "intermedio"})) #observar que json es en formato diccionario