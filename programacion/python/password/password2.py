print("INSTRUCCIONES")
print("1. La longitud del password debe ser superior a 6 caracteres")
print("2. Deben aparecer almenos dos números")
print("uno entre el 1 y el 5 y otro entre 6 y 9")
print("3. Deben aparecer almenos dos minúsculas")
print("4. Debe aparecer almenos una mayúscula")
print("5. Debe aparecer almenos dos de estos símbolos: @,#,$,(,),¿,?,¡,!,&,=,%,/")
print("6. tienes 3 intentos")
pos=0
neg=0
lou=0
sim=0


for contador in range(3):  #repito la pregunta 3 veces  
    lou=0   #Inicializo variables
    sim=0
    num=False
    correco=False
    numero4=False     #numero entre 1 y 5
    numero7=False     #numero entre 6 y 9
    upp=False         #mayusculas
    simbol=False      #simbolos
    minu=False        #minusculas
    leng=False        #longitud
    pas=input("introduce la contrasenya: ")
    lon=len(pas)  
    for recorrer in pas:   #segundo bucle, revisa la contraseña por letras
        if recorrer.islower():
            lou+=1     #cuento minusculas
        if recorrer.isupper():
            upp=True
        if recorrer.isnumeric():                  #compruebo que los numeros estan en el rango
            if int(recorrer)>=1 and int(recorrer)<=5:
                numero4=True
            if int(recorrer)>=6 and int(recorrer)<=9:
                numero7=True
        if recorrer in "@#~,?¿!¡&=%/$":    #compruebo si los simbolos son parte de la lista
            sim+=1
        if lou>=2:
            minu=True   #si hay mas de 2 minusculas esa parte se cunple
        if numero4==True and numero7==True :
            num=True
        if lon>=6:      #compruebo longitud
            leng=True
        if sim>=2:      #compruebo los 2 simbolos
            simbol=True
        if upp==True and simbol==True and minu==True and numero4==True and numero7==True and leng==True:   
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
        if num==False :
            print("los numeros no se cumplen")
        if simbol==False:
            print("faltan simbolos")
print(neg,"contraseñas eran incorrectas")            #recuento de contraseñas
print(pos,"contraseñas eran correctas")
        
       
