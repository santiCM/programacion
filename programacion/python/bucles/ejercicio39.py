rep=int(input("¿cuantos numeros vas a introducir?: "))
pos=0
neg=0
cer=0
for cont in range(rep):
    num=int(input("introduce un numero: "))
    if num<0:
        neg+=1
    if num==0:
        cer+=1
    if num>0:
        pos+=1

print("La cantidad de números positivos es:", pos)
print("La cantidad de números negativos es:", neg)
print("La cantidad de números ceros es:", cer)
        