lista=[]
vocales=[]
rep=""
while rep!="n" :
    letra=input("Introduce una letra ")
    if letra.isalpha:
        if not letra in vocales:
            lista.append(letra) 
        if letra in ("aáà"):
            vocales.append("a")
            vocales.append("á")
            vocales.append("à")   
        if letra in ("iíì"):
            vocales.append("i")
            vocales.append("í")
            vocales.append("ì")
        if letra in ("uúù"):
            vocales.append("u")
            vocales.append("ú")
            vocales.append("ù")
        if letra in ("eéè"):
            vocales.append("e")
            vocales.append("é")
            vocales.append("è")
        if letra in ("oóò"):
            vocales.append("o")
            vocales.append("ó")
            vocales.append("ò")    
    else:
        letra=""
    rep=input("quieres repetir? (s/n) ")
lista=set(lista)
print(lista)