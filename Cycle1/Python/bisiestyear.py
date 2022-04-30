#Ingrese un año y un mes y determine si es un año bisiesto

from types import ModuleType


year = int(input("Ingrese el anho que desea consultar"))
month = int(input("Ingrese el numero del mes que desea saber"))

if year % 4 == 0 or year % 100 == 0:
    if year % 400 != 0:
        print("Es bisiesto")
        if month == 2:
            print("Tiene 29 dias")
        elif month == 4 or month == 6 or month == 9 or month == 11:
            print("Tiene 30 dias")
        else:
            print("Tiene 31 dias")
    else:
        print("No es bisiesto")
else:
    print("No es bisiesto")
