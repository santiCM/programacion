import random
rep=""
respuesta=""
numero=0
jtotal=0
btotal=0
palos= [1,2,3,4,5,6,7,10,11,12]
Banca=False
puntos=100
print("que comience la partida")
nombre=input("Introduce tu nombre: ")
carta=input("quieres carta? (s/n): ")
if carta=="s":
    numero=random.choice(palos)
    if numero==10 or numero==11 or numero==12:
        jtotal+=0.5
        print(f"{nombre}, tu carta es: {numero}")
        print("el total acumulado es: ",jtotal)
    else:
        jtotal+=numero
        print(f"{nombre}, tu carta es: {numero}")
        print("el total acumulado es: ",jtotal)
if carta=="n":
    print("AWENO")
    respuesta="n"
    repeticiones=0


while carta=="s" and jtotal<7.5:
    respuesta="n"
    print("tus puntos: ", puntos)
    if puntos>0:
        
        carta=input("quieres carta? (s/n): ")
    else:
        carta="n"
        repeticiones="n"
        print("NO TE QUEDAN PUNTOS")
    if carta=="s":
        numero=random.choice(palos)
        if numero==10 or numero==11 or numero==12:
            jtotal+=0.5
            print(f"{nombre}, tu carta es: {numero}")
            print("{nombre}, el total acumulado es: ",jtotal)
        else:
            jtotal+=numero
            print(f"{nombre}, tu carta es: {numero}")
            print("{nombre}, el total acumulado es: ",jtotal)
        if jtotal>7.5:
            print("Te has pasado")
            Banca=True
            puntos-=10
            carta="n"
       
    if carta=="n":
        if jtotal<6:
            print("Quizás tendrías que arriesgar un poco ¿no?")
            puntos-=5  
            Banca=True
        if jtotal>=6 and jtotal<=7:
            print("Has sido un poco conservador")
            Banca=True
            puntos+=5
    if carta!="s" and carta!="n" :
        print("esa respuesta no es valida")
else:
    carta="s"
    while Banca==True:
        if carta=="n" :
            Banca=False
        if carta=="s":    
            numero=random.choice(palos)
            if numero==10 or numero==11 or numero==12:
                btotal+=0.5
                print(f"la carta es: {numero}")
                print("el total acumulado es: ",btotal)
            else:
                btotal+=numero
                print(f"la carta es: {numero}")
                print("el total acumulado es: ",btotal)
            if btotal<6:
                carta="s"
            if btotal==7.5:
                if btotal==jtotal:
                    print("Empate")
                if jtotal>btotal:
                    print("Gana la banca")
                if jtotal<btotal:
                    print("Gana la banca")
            if btotal>=7 and btotal<=7.5:
                carta="n"
                
            if btotal>7.5 :
                carta="n"
                Banca=False
            
    else:
        print("{nombre}, el total acumulado es: ",jtotal)
        print("el total acumulado por la banca es: ",btotal)  
        Banca=False
        if jtotal==7.5 and btotal!=7.5:
            print(f"Gana {nombre}")
        if btotal==7.5 and jtotal!=7.5:
            print("Gana la banca")
        if jtotal>=7.5 and btotal<jtotal :
            print(f"Gana {nombre}")
        if jtotal>=7.5 and btotal>7.5 :
            print(f"Gana {nombre}")
        if btotal>=7.5 and jtotal<btotal :
            print(f"Gana la banca")
        if btotal>=7.5 and jtotal>7.5 :
            print(f"Gana la banca")
        if btotal<7.5 and jtotal<7.5 and btotal>jtotal:
            print("Gana la banca")
    
