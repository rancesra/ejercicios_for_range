inicio = int(input("ingrese el rango desde donde inicia: "))
fin  = int(input("ingrese el rango donde termina: "))

multiplo7 = 0
multiplo9 = 0
normales = 0

for i in range(inicio,fin):
    if i % 7 == 0:
        multiplo7 = multiplo7+1
    else:
        if i % 9 == 0:
            multiplo9 = multiplo9+1
        else:
            normales = normales+1


print("cantidad de multiplos de 7: ",str(multiplo7))

print("cantidad de multiplos de 9: ",str(multiplo9))

print("cantidad de numeros normales: ",str(normales))