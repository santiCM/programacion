print("1. La longitud del passwordt� que tenir entre 6 i 8 car�cters")
print("2. For�a els seg�ents valors segons la posici� indicada:")
print("Posici�n 1 Un n�mero mayor o igual 1 y menor o igual que 5")
print("Posici�n 2 Una letra min�scula")
print("Posici�n 3 Una letra may�scula")
print("Posici�n 4 Uno de los siguientes s�mbolos @")
print("Posici�n 5 Una letra min�scula")
print("Posici�n 6 Un n�mero mayor o igual 6 y menor o igual que 9")
print("Posici�n 7 Uno de los siguientes s�mbolos &,/,#")
print("Posici�n 8 Un n�mero menor o igual que 5")

password=input("introduce la contrasenya: ")
lon=len(password)


if lon<6 or lon>8:
    print(f"Error, el password tiene una longitud de {lon} caracters i no compleix els requisits")
elif int(password[0])>5 or int(password[0])<1:
    print("Error en el caracter 1")
elif password[1].isupper():
    print("Error en el caracter 2")
elif password[2].islower():
    print("Error en el caracter 3")
elif not password[3] == "_" or password[3]=="@" or password[3]== "*":
    print("Error en el caracter 4")
elif password[4].isupper():
    print("Error en el caracter 5")
elif int(password[5])>9 or int(password[5])<6:
    print("Error en el caracter 6")
else:    
    if lon == 7:
        if not password[6]=="&" or password[6]=="/" or password[6]=="#":
            print("Error en el caracter 7")
if lon == 8:
    if int(password[7])>5:
        print("Error en el caracter 8")
else:
    print("El format del PASSWORD es correcte")