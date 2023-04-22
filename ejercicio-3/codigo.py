import random

cantidaddados = int(input("ingrese el numero de dados que desea lanzar: "))
cara1 = []
cara2 = []
cara3 = []
cara4 = []
cara5 = []
cara6 = []

for i in range(cantidaddados):
    numerorandom = random.randint(1,6)
    if numerorandom == 1:
        cara1.append('*')
    else:
        if numerorandom == 2:
            cara2.append('*')
        else:
            if numerorandom == 3:
                cara3.append('*')
            else:
                if numerorandom == 4:
                    cara4.append('*')
                else:
                    if numerorandom == 5:
                        cara5.append('*')
                    else:
                        cara6.append('*')





print("cara1: ",cara1)
print("cara2: ",cara2)
print("cara3: ",cara3)
print("cara4: ",cara4)
print("cara5: ",cara5)
print("cara6: ",cara6)