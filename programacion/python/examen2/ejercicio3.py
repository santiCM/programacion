
total=0
cif=int(input("introduce un numero de cifras "))
num=input("introduce un numero ")
if len(num)!= cif:
    print("error, el numero de cifras no coincide")
if len(num)==cif:
    for recorer in num:
        total=int(total+int(recorer))
    print("resultado", total)