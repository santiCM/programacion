#Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. 
# Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.

import math
diam=int(input("dame un numero:" ))
rad=diam/2
area=float((rad**2)*(math.pi))
area=round(area, 1)
perimetro=float(2*(math.pi)*rad)
perimetro=round(perimetro,1)
print("el area es:",area)
print("el perimetro es:",perimetro)
