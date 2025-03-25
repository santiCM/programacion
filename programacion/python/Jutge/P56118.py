
var=input()
lista=var.split()
maximo=int(lista[1])
for recorrer in lista:
    if int(recorrer)>maximo:
        maximo=int(recorrer)

print(maximo)




