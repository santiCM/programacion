#las variables no pueden empezar por numeros
var1=float(input("Introduce el peso: "))
#hay que definirlo como int o float
var2=float(input("Introduce la altura: "))
#solo un simbolo igual para definir variables
var_imc=var1 / var2**2
print("Si pesas {1Var} kilos y mides {2var}, tu IMC es:",
var_imc)
#faltan los ":"
if var_imc>25:
 print("Hay sobrepeso")
else:
 print("Estás dentro de los parámetros normales")