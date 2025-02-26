txt="a,b,D,x,r,X,3,h,w,2,i"
lista1=txt.split(",")
letras=[]
numeros=[]
leng=len(lista1)

for recorrer in lista1:
    if recorrer.isnumeric():
        numeros.append(recorrer)
    if recorrer.isalpha():
        letras.append(recorrer)
reverse=int(input("Introduce 1 para visualizar en orden ascendente o 2 descendente: 1"))
if reverse==1:
    letras.sort()
    numeros.sort()
if reverse==2:
    letras.sort(reverse=True, key=str.lower)
    numeros.sort(reverse=True)
print(numeros)
print(letras)