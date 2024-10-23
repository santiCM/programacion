letra=input("introduce una letra ")
if letra.isupper():
    print("la letra es mayuscula")
elif letra.islower():
    print("la letra es minuscula")
elif letra.isdigit():
    print("el valor era un numero")
else:
    print("el valor era un simbolo")
