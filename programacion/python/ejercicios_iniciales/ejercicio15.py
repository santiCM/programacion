import math
rad=int(input("dame un numero:" ))
hi=int(input("dame otro:" ))
vol=(math.pi)*(rad**2)*hi
area=(2*(math.pi)*rad*hi)+(2*(math.pi)*(rad**2))
vol=round(vol,2)
area=round(area,2)
print("el area del cilindro es", area)
print("el volumen del cilindro es", vol)