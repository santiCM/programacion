lista=[]

repeticiones=int(input("Introduce el numero de palabras a introducir: "))
for contador in range(repeticiones):
    pal=input(f"introduce la {contador+1}ª palabra ")
    lista.append(pal)
copia=lista.copy()
copia.reverse()
print(lista)
print(copia)