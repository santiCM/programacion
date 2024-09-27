import math
diam=int(input("dame un numero:" ))
rad=diam/2
area=float((rad**2)*(math.pi))
area=round(area, 1)
perimetro=float(2*(math.pi)*rad)
perimetro=round(perimetro,1)
print("el area es:",area)
print("el perimetro es:",perimetro)
