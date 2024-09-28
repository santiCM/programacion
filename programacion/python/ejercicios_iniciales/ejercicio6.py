#A partir del programa 5. Haz que se muestre por pantalla también la frase en el orden inverso en que se han introducido las palabras
pal1=str(input("introduce una palabra: "))
pal2=str(input("introduce otra palabra: "))
pal3=str(input("introduce otra: "))
pal4=str(input("introduce otra mas: "))
pal5=str(input("introduce una ultima palabra: "))
frase=pal1+pal2+pal3+pal4+pal5
print(frase)
print(f"{pal5},{pal4},{pal3},{pal2},{pal1}")