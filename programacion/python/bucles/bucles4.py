num=int(input("introduce el numero: "))
for contador in range(1,10+1):
    res=num*contador
    if res>40:
        print(f"el resultado de {num}*{contador} es mayor a 40")
        break
    else:
        print(res)
