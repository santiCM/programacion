#Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El
#resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un
#resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso
#(raíz y división)
import math
var1=int(input("introduce un numero: "))
raiz=(math.sqrt(var1))
raiz=round(raiz,1)
divi=raiz/2
divi=(math.floor(divi))
print("la raiz es:", raiz)
print("la division es:", divi)