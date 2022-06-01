number = int(input("Ingrese el numero que quiere saber el factorial"))

f = 1
for i in range(1,number + 1):
    f = f * i
    print(f"El factorial es {f}")