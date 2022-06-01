print("Ingrese cuantas veces quiere repetir el ciclo para ingresar el numero")
manytimes = int(input())

for i in range(manytimes):
    print("Ingresemos un numero")
    num = int(input())
    if num != 0:
        if num > 0:
            print("Es positivo")
        else:
            print("Es negativo")
    else:
        print("Es cero")