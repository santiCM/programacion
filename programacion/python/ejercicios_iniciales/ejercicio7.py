#programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?

operador1=float(input("introduce un numero: "))
operador2=float(input("introduce otro: "))
suma=float(operador1+operador2)
resta=float(operador1-operador2)
multi=float(operador1*operador2)
divi=float(operador1/operador2)
expo=float(operador1**operador2)
diven=float(operador1//operador2)
ronda=round(divi, 2)
print(f"La suma de {operador1} y {operador2} es:", suma)
print(f"La resta de {operador1} y {operador2} es:", resta)
print(f"La multiplicación de {operador1} y {operador2} es:", multi)
print(f"la division de {operador1} y {operador2} es:", ronda)
print(f"El exponente de {operador1} y {operador2} es:", expo)
print(f"La división entera de {operador1} y {operador2} es:", diven)
