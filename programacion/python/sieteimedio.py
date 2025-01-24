import random
numero=0
total=0
palos= [1,2,3,4,5,6,7,10,11,12]
print("que comience la partida")
while respuesta!="n":
    numero=random.choice(palos)
    if numero==10 or numero==11 or numero==12:
        total+=0.5
    else:
        total+=numero
    print(f"tu carta es: {numero}")
    print("el total acumulado es: ",total)
    
    
    if total<7.5:
        rep=input("quieres otra carta? (s/n) ")
    elif total==7.5:
        print("Enhorabuena, has ganado la partida")
        respuesta=input("quieres repetir una nueva partida?")
    else:
        print("Has perdido la partida!")
        respuesta=input("quieres repetir una nueva partida?")
        
    if rep=="n":
        if total<6:
            print("Quizás tendrías que arriesgar un poco ¿no?")
        if total>=6 and total<=7:
            print("Has sido un poco conservador")