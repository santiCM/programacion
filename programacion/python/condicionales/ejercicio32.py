frase="A quién madruga Dios ayuda"
palabra=input()

fraseb=frase.casefold()

lugar=fraseb.find(palabra.casefold())


if lugar<0:
    print("esa palabra no esta en la frase")
else:
    print(lugar)