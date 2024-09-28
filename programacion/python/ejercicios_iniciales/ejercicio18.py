#Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan
#importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores
#de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por
#teclado el número de menores y el número de adultos que asisten al cine.
import math
adult=int(input("¿cuantos adultos seran?:" ))
nin=int(input("¿y cuantos niños?:" ))
precioa=(adult*12)-(adult*1.2)
precion=(nin*12)/2
print(f"El precio total del cine para {nin} menor/es es", precion)
print(f"El precio total del cine para {adult} adulto/s es", precioa)