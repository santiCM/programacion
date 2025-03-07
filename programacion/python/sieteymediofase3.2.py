import random
rep=""
respuesta=""
numero=0
jtotal=0
btotal=0
palos= [1,2,3,4,5,6,7,10,11,12]
Banca=True
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
        carta="s"
if jtotal==7.5:
    print("Enhorabuena, has obtenido 7.5")
    carta="n"
    Banca=True
print("Ahora es el turno de la banca, pulsa enter para continuar")

carta="s"
while Banca==True:
    input()
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
            if btotal<=6 :
                if jtotal>btotal:
                    carta="s"
                if jtotal<btotal:
                    carta="n"
                if jtotal==0:
                    carta="s"
            elif btotal>=7 and btotal<8:
                if jtotal!=7.5:
                    carta="n"
                elif jtotal==7.5:
                    carta="s"
                elif jtotal<btotal:
                    carta="n"
            elif jtotal>7.5:
                if btotal<5:
                    carta="s"
                else:
                    carta="n"
            elif jtotal>btotal:
                if btotal==7.5:
                    carta="n"
                elif btotal<6 and jtotal>7.5:
                    carta="s"
            elif btotal==7:
                if jtotal<btotal:
                    carta="n"
            elif btotal>7.5:
                carta="n"
            elif jtotal<btotal and btotal<5:
                carta="n"
            elif btotal==7.5:
                carta="n"
                banca=False 
        if carta=="n" :
            Banca=False
print("la partida se acaba")
if btotal>jtotal:
    if jtotal<8 and btotal<8 or btotal==7.5:
        print("Gana la banca")
    if jtotal<7.5 and btotal>7.5:
        print(f"Gana {nombre}")
if btotal==jtotal:
    if jtotal<8 and btotal<8:
        print("empate, Gana la banca")
if btotal>7.5 and jtotal>7.5:
    print(f"Pierden {nombre} y banca")
if btotal<jtotal:
    if jtotal>7.5 and btotal<=7.5:
        print("Gana la banca")
    if btotal>7.5 and jtotal<=7.5:
        print(f"Gana {nombre}")
        
         
