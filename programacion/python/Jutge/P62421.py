concatenar=""
txt=input()
texto=txt.split( )
for recorrer in texto:
    
    concatenar=recorrer+" "+ concatenar
print(concatenar[:-1])