#Programa que pida cinco palabras y muestre una frase con las cinco. Modifica el código para que entre palabra y palabra haya una coma
pal1=str(input("introduce una palabra: "))
pal2=str(input("introduce otra palabra: "))
pal3=str(input("introduce otra: "))
pal4=str(input("introduce otra mas: "))
pal5=str(input("introduce una ultima palabra: "))
frase=pal1+pal2+pal3+pal4+pal5
print(frase)
print(f"{pal1},{pal2},{pal3},{pal4},{pal5}")
