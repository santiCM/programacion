import math
peso=int(input("dime cuanto pesas en quilos: "))
alt=float(input("y ahora cuanto mides en metros: "))
imc=peso/(alt**2)
imc=round(imc,2)
if imc>25:
    print(f"si pesas {peso} quilos y mides {alt} metros tu imc es de {imc}. hay sobrepeso")
else:
    print(f"si pesas {peso} quilos y mides {alt} metros tu imc es de {imc}.")