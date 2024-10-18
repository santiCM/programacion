# Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
nota=float(input("Introduce la nota "))

if nota>10 or nota<0:
    print("La nota que has introducido no está entre 0 y 10")
else:
    if nota>5 or nota==5:
        print(f"has sacado un {nota} y has aprobado")
    if nota<5:
        print(f"has sacado un {nota} y has suspendido")
