
def factorial(n):
    f = 1

    for i in range(1,n):
        f = f * (i+1)

    return f

def main():
    n = int(input("Ingrese el numero total de elementos"))
    r = int(input("Ingrese el numero de elementos a combinar"))
    result = factorial(n)
    combinatory = factorial(n) / (factorial(n-r) * factorial(r))

    print(f"The combinatory of numbers are: {combinatory}")
    

if __name__ == "__main__":
    main()