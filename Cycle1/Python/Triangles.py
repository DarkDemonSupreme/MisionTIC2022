
"""7 Dados 3 valores enteros X, Y, Z. Elaborar un algoritmo para determinar si esos valores son los lados de un triángulo. 
 X, Y, Z, son los lados de un triángulo si cumplen con las siguientes condiciones:       
 X>0,  Y>0,  Z>0,  X+Y>Z,  X+Z>Y,  Y+Z>X 
 Además, clasificar el triángulo por sus lados: Equilátero, Escaleno e Isósceles """

x = float(input("Ingrese el lado X"))
y = float(input("Ingrese el lado Y"))
z = float(input("Ingrese el lado Z"))

if x > 0 and y > 0 and z > 0 and x+y>z and x+z>y and y+z>x:
    print("Es un triangulo")
    if x == y == z:
        print("Es un triangulo equilatero")
    elif x == y or x == z or y == z:
        print("Es un triangulo isosceles")
    else:
        print("Es un triangulo escaleno")
else:
    print("No es un triangulo")