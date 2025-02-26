lista=[]
repeticiones=int(input("Introduce el numero de valores a introducir: "))
for contador in range(repeticiones):
    numero=int(input("introduce un numero: "))
    lista.append(numero)
    lista.sort()
print(lista)
    