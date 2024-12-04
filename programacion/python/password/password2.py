print("INSTRUCCIONES")
print("1. La longitud del password debe ser superior a 6 caracteres")
print("2. Deben aparecer almenos dos números")
print("3. Deben aparecer almenos dos minúsculas")
print("4. Debe aparecer almenos una mayúscula")
print("5. Debe aparecer almenos uno de estos símbolos: @,#,$,(,),¿,?,¡,!,&,=,%,/")
print("6. tienes 3 intentos")
pos=0
neg=0
lou=0
numer=0
correco=False

for contador in range(3):  #repito la pregunta 3 veces  
    lou=0   #Inicializo variables
    numer=0
    upp=False 
    simbol=False 
    minu=False 
    num=False 
    leng=False
    pas=input("introduce la contrasenya: ")
    lon=len(pas)  
    for recorrer in pas:
        if recorrer.islower():
            lou+=1     #cuento minusculas
        if recorrer.isupper():
            upp=True
        if recorrer.isnumeric():
            numer+=1    #cuento numeros
        if recorrer in "@#~,?¿!¡&=%/":
            simbol=True
        if lou>=2:
            minu=True   #si hay mas de 2 minusculas esa parte se cunple
        if lon>=6:
            leng=True
        if numer>=2:
            num=True
        if upp==True and simbol==True and minu==True and num==True and leng==True:   
            correco=True    #si cumple con todo correco es true
            print("La contrasenya es correcta")
            pos+=1
            break        
    if leng==False:
        print("la contraseña es demasiado corta")
    if not correco:
        print("la contrasenya es incorrecta")   
        neg+=1
        if upp==False:
            print("faltan mayusculas")   #reviso lo que falla y digo el error
        if minu==False:
            print("faltan minusculas")
        if num==False:
            print("faltan numeros")
        if simbol==False:
            print("faltan simbolos")
print(neg,"contraseñas eran incorrectas")
print(pos,"contraseñas eran correctas")
        
       
