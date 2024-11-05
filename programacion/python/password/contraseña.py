password=input("introduce la contraseña: ")
lon=len(password)
va0=int(password[0])
va1=password[1]
va2=password[2]
va3=str(password[3])
va4=password[4]
va5=int(password[5])
va6=str(password[6])
va7=int(password[7])

if lon<6 or lon>8:
    print(f"Error, el password tiene una longitud de {lon} caracters i no compleix els requisits")
elif va0>5 or va0<1:
    print("Error en el caracter 1")
elif va1.isupper():
    print("Error en el caracter 2")
elif va2.islower():
    print("Error en el caracter 3")
elif va3!= "*" or va3!= "_" or va3!="@" :
    print("Error en el caracter 4")
elif va4.isupper():
    print("Error en el caracter 5")
elif va5>9 or va5<6:
    print("Error en el caracter 6")
elif va6!="&" or va6!="/" or va6!="#":
    print("Error en el caracter 7")
elif va7>5:
    print("Error en el caracter 8")
else:
    print("El format del PASSWORD es correcte")