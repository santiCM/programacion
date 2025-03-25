var=input()

lista=var.split()
if len(lista)<2:
    var=input()
    lista.append(var)
suma=int(lista[0])+int(lista[1])
print(suma)