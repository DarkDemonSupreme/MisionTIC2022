def find_values(x):
    return x**3 + (x/2) + 1

n = int(input("Define el rango"))

for i in range(-n,n +1):
    result = find_values(i)
    print(f"Para x vale {i} su valor en y es {result}")