par=0
imp=0
for contador in range(50):
    if contador%2==0:
        par+=1
    if contador%2!=0:
        imp+=1
print("El total de pares es:", par)
print("El total de impares es:", imp)
        