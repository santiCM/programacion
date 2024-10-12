nota=float(input("Introduce la nota "))

if nota>10 or nota<0:
    print("La nota que has introducido no está entre 0 y 10")
else:
    if nota>8.5:
        print(f"tu nota es {nota}, has sacado un excelente")
    if nota>6.5 and nota<8.5 or nota==8.5:
        print(f"tu nota es {nota}, has sacado un notable")
    if nota>5 and nota<6.5 or nota==6.5:
        print(f"tu nota es {nota}, has sacado un satisfactorio")
    if nota<5:
        print(f"tu nota es {nota} has sacado un insuficiente")

  