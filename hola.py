edad = 17
estado = "Mayor de edad" if (edad >= 18) else "Menor de edad"

print(estado) # Salida: Mayor de edad


while edad>=25:
    if(edad>=10):
        edad+= 2
        print(f"avanza y de la nada tienes {edad}")
    else:
        edad+=1
        print(f"avanza y de la nada tienes {edad}")

