txt="a,b,D,x,r,X,3,h,w,2,i"
lista1=txt.split(",")
leng=len(lista1)
numeros=0
total=0
letras=0
mayus=0
for recorrer in lista1:
    if recorrer.isnumeric():
        numeros+=1
        total+=int(recorrer)
    if recorrer.isalpha():
        letras+=1
        if recorrer.isupper():
            mayus+=1

print(f"Número de valores: {leng}" )
print(f"Cantidad de números: {numeros}" )
print(f"cantidad de letras: {letras}" )
print(f"cantidad de mayusculas: {mayus}" )
print(f"suma total de numeros: {total}" )
