# ----------------------- NIVEL 5 ------------------------------

    #Ejercicio 25 Sistema de Calificaciones

cantidad_notas= int(input("Cuantas notas tienes: "))
List_notas=[]
suma=0
i=0

while i < cantidad_notas:
    try:
        nota=float(input("Ingrese la nota: "))
        porcentaje= int(input("cual es el porcentaje al que equivale la nota: "))
        if (nota<0 or nota>5) or (porcentaje<=0) or (porcentaje>100):
            raise ValueError("La nota o porcentaje es invalido")
    except ValueError:
        print("Esa nota que ingresaste es inválida o el porcentaje es inválido")
    else:  #se ejecuta solo sí el try funcionó
        List_notas.append(nota) #agrega la nota a la lista
        nota= (nota* (porcentaje/100)) #Saca el porcentaje de nota multiplica con la nota
        suma+= nota  #va sumando el valor de cada nota
        i+=1        # aumenta el contador para limitar iteraciones

print(f"List_notas es la siguiente: {List_notas}")

if ((suma>=0) and (suma < 3)):
    print(f"Haz reprobado tu nota fue {suma}")
elif ((suma>0) and (suma < 5)):
    print(f"Acabas de aprobar, tu nota fue {suma}, felicidades!")
elif suma == 5:
    print(f"FELICITACIONES tu nota fue la mejor de la clase, sacaste {suma}, lo hiciste excelente")



