import random
rep=""
respuesta=""
numero=0
total=0
palos= [1,2,3,4,5,6,7,10,11,12]
repeticiones=1
print("que comience la partida")

carta=input("quieres carta? (s/n): ")
if carta=="s":
    numero=random.choice(palos)
    if numero==10 or numero==11 or numero==12:
        total+=0.5
        print(f"tu carta es: {numero}")
        print("el total acumulado es: ",total)
    else:
        total+=numero
        print(f"tu carta es: {numero}")
        print("el total acumulado es: ",total)
while carta=="s" or total<7.5 and respuesta!="n":
    respuesta="n"
    carta=input("quieres carta? (s/n): ")
    
    if carta=="s":
        numero=random.choice(palos)
        if numero==10 or numero==11 or numero==12:
            total+=0.5
            print(f"tu carta es: {numero}")
            print("el total acumulado es: ",total)
        else:
            total+=numero
            print(f"tu carta es: {numero}")
            print("el total acumulado es: ",total)
        if total>7.5:
            print("Has perdido la partida!")
            respuesta=input("quieres repetir una nueva partida?(s/n) ")
            carta="n"
        if total==7.5:
            print("Enhorabuena, has ganado la partida(s/n) ")
            respuesta=input("quieres repetir una nueva partida?(s/n) ")
            carta="n"
        if respuesta=="s":
            total=0
            carta="s"
    if carta=="n":
        if total<6:
            print("Quizás tendrías que arriesgar un poco ¿no?")
            respuesta=input("quieres repetir una nueva partida?(s/n) ")
        if total>=6 and total<=7:
            print("Has sido un poco conservador")
            respuesta=input("quieres repetir una nueva partida?(s/n)")  
       
    if respuesta=="s":
        repeticiones+=1
        total=0
        carta="s"
else:
    print(f"has jugado {repeticiones} partidas")
