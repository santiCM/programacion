var=input()

lista=var.split()
while len(lista)<3:
    if len(lista)<3:    
        var=input()
        if var.isnumeric():
            lista.append(var)
suma=int(lista[0])+int(lista[1])+int(lista[2])
print(suma)