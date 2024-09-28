#Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.
num1=float(input("Dame un numero: "))
num2=float(input("dame otro: "))
cociente=num1/num2
resto=num1%num2

def dividendo (n):
    if num1%2==0:
        return "el dividendo es par"
    else:
        return"el dividendo es impar"

print("el cociente es:", cociente)
print("el resto es:", resto)
print(dividendo (num1))