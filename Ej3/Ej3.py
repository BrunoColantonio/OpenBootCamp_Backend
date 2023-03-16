peso = input("Ingrese su peso en kg: ")
estatura = input("Ingrese su estatura en metros: ")
peso = float(peso)
estatura = float(estatura)

indice = (peso) / (estatura ** 2)
indice = round(indice, 2)

print("Tu índice de masa corporal es: ", indice)


