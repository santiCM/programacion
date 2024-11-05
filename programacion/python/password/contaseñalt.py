print("1. La longitud del passwordté que tenir entre 6 i 8 caràcters")
print("2. Força els següents valors segons la posició indicada:")
print("Posición 1 Un número mayor o igual 1 y menor o igual que 5")
print("Posición 2 Una letra minúscula")
print("Posición 3 Una letra mayúscula")
print("Posición 4 Uno de los siguientes símbolos @")
print("Posición 5 Una letra minúscula")
print("Posición 6 Un número mayor o igual 6 y menor o igual que 9")
print("Posición 7 Uno de los siguientes símbolos &,/,#")
print("Posición 8 Un número menor o igual que 5")

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