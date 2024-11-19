rep=int(input("¿Cuantas notas vas a introducir?: "))
for cont in range(rep):
    nota=float(input("introduce la nota: "))
    if nota>=5 and nota<=10:
        print("asignatura aprobada")
    if nota<5 and nota>=0:
        print("asignatura suspendida")
    if nota>10 or nota<0:
        print("Valor incorrecto")
        