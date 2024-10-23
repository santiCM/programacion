frase="A quién madruga Dios ayuda"
palabra=input()
lugar=frase.find(palabra)
if lugar<0:
    print("esa palabra no esta en la frase")
else:
    print(lugar)