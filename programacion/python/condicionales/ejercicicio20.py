#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
var1=int(input("introduce un numero "))
var2=int(input("introduce otro "))
if var1>10 or var2>10:
    print("Uno o los dos números están fuera de los límites establecidos")
else:
    if var1>var2:
        print(f"{var1} es mayor que {var2}")

    if var2>var1:
        print(f"{var2} es mayor que {var1}")

    if var1==var2:
        print("ambos son iguales")
