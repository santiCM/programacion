# Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math
var1=int(input("introduce un numero "))
var2=int(input("introduce otro "))
var3=int(input(" introduce otro "))
raiz=(var2**2-4*var1*var3)
if raiz<0:
    print("La raíz no puede ser un valor negativo")
else:
    equacion1=((var2*-1)+math.sqrt(var2**2-4*var1*var3))/(2*var1)
    equacion2=((var2*-1)-math.sqrt(var2**2-4*var1*var3))/(2*var1)
        
    print(f"el valor de x1 es {equacion1}")
    print(f"el valor de x2 es {equacion2}")
