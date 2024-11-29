prec=0
desc=0
print("""Gasolinera
1.sin plomo 95
2.sin plomo 98
3.Gasoleo A
4.Gasoleo A+""")

comb=int(input("escoja el tipo de combustible "))
cant=int(input("introduzca el numero a repostar "))
if comb==1:
    prec=1.765*cant
if comb==2:
    prec=1.913*cant
    total=prec-((prec*10 )/100)
if comb==3:
    prec=1.746*cant
if comb==4:
    prec=1.839*cant
    total=prec-(prec*12/100)
if comb==1 or comb==3:
    print(f"el total a pagar es {prec}")
if comb==2 or comb==4:
    print(f"el total a pagar es {prec} y con e descuento es {total}")