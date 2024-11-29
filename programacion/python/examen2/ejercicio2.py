pos=0
neg=0

for contador in range(6):
    val=int(input("introduce un numero: "))
    if val>0:
        pos+=val
    if val<0:
        neg+=val
        
print(f"la suma de positivos es {pos}")
print(f"la suma de negativos es {neg}")