lista=[]
rep=""
while rep!="n" :
    letra=input("Introduce una letra ")
    if letra.isalpha:
        lista.append(letra)
    else:
        letra=""
    rep=input("quieres repetir? (s/n) ")
lista=set(lista)
print(lista)