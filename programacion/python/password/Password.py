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
#inc es un chivato que se vuelve true en cuanto detecte un error
inc=False
#err acumula los errores que detecta y al final los dice todos
err="-"
if lon<6 or lon>8:
    print(f"Error, el password tiene una longitud de {lon} caracters i no compleix els requisits")
if password[0] not in "12345":
    inc=True
    err=err+"Error en el caracter 1 "
if not password[1].islower():
    inc=True
    err=err+"Error en el caracter 2 "
if not password[2].isupper():
    inc=True
    err=err+"Error en el caracter 3 "
if password[3] not in "*_&":
    inc=True
    err=err+"Error en el caracter 4 "
if not password[4].islower():
    inc=True
    err=err+"Error en el caracter 5 "
if password[5] not in "6789":
    inc=True
    err=err+"Error en el caracter 6 "
if lon == 7:
    if password[6] not in "&/#":
        inc=True
        err=err+"Error en el caracter 7 "
if lon == 8:
    if int(password[7])>5:
        inc=True
        err=err+"Error en el caracter 8 "
if not inc:
    print("El format del PASSWORD es correcte")
else:
    print(err)
