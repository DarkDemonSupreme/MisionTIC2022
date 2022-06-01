""" 
def materias(materias_ingresadas:str):
    materias_separadas = []
    for i in materias_ingresadas.split(","):
        materias_separadas.append(i)
    return materias_separadas

print (materias("Inglés,Física,Sociales,Historia,Programación"))
 """
""" def listaFrutas(frutas):
    for i in frutas:
        print(i)

print(listaFrutas(["Manzana", "Uva", "Aguacate"]))

def multiplicarNumeros(numeros_Multiplicadores):
    result = 1
    for i in numeros_Multiplicadores:
        result *= i
    return result

print(multiplicarNumeros([2,3,5]))  """



mi_diccionario = {"Nombre": "Deiby Montenegro","Edad": 21, "Ocupacion": "Programador"} 

print(mi_diccionario)

for i in mi_diccionario.values():
    print(i)