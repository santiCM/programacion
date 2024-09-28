#. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
lado=int(input("introduce la medida del lado:" ))
basem=int(input("introduce la medida de la base menor:" ))
baseM=int(input("introduce la medida de la base mayor:" ))
hi=int(input("introduce la altura:" ))
peri=lado+basem+baseM+lado
area=((baseM+basem)/2)*hi
print("el perimetro es:", peri)
print("el area es:", area)