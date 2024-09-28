#programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
secs=int(input("introduce un numero de segundos: "))
mins=secs/60
horas=mins/60
horas=round(horas, 2)
print(f"el número de minutos es: {mins} y en horas es: {horas}")
