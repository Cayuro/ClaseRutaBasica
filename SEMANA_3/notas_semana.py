import math
import random
import datetime

print("Raíz de 16: ", int(math.sqrt(16)))
print("Número aleatorio entre 1 y 10: ", random.randint(1,10))
print("Fecha de hoy: ", datetime.date.today())
print(datetime.datetime.now())

try: 
    num1= int(input("Ingrese un numero: "))
except ValueError:
    print("Mal, eso no es un numero")
finally:
    print("Saliendo del programa")