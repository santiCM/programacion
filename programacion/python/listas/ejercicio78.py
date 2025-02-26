txt="a,b,D,x,r,X,3,h,w,2,i"
lista1=txt.split(",")
valor=input("introduce el valor que deseas eliminar: ")
if valor in lista1:
    if valor.isnumeric:
        lista1.remove(valor)
        print(lista1)
    else:
        print("Introduce valor numérico")
else:
    print("El valor introducido no está en la lista")
rep=input("deseas repetir? (s/n): ")
while rep!="n" :
    valor=input("introduce el valor que deseas eliminar: ")
    if valor in lista1:
        if valor.isnumeric:
            lista1.remove(valor)
            print(lista1)
        else:
            print("Introduce valor numérico")
    else:
        print("El valor introducido no está en la lista")
    rep=input("deseas repetir? (s/n): ")