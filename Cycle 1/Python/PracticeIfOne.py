a = float(input("Ingrese el numero A "))
b = float(input("Ingrese el numero B "))

c = a - b 

if c == 0:
    print("Los numeros restados dan cero")
elif c < 0:
    print(f"El numero {c} es negativo")
else:
    print(f"El numero {c} no es negativo")
