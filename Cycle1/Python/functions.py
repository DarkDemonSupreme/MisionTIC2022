import os 
from glob import glob
from math import factorial, sin,cos,tan, pi 
import random
import datetime
from ssl import OPENSSL_VERSION_NUMBER
print(os.getcwd())
number_list = [53, 90, 23, 80, 11, 0]

print(glob('.' + '/*.py'))
a = 1
b = 15
print("El numero mas grande es: ", max(number_list))
print("La lista ordenada es: ", sorted(number_list))
print("El largo de la lista es : ", len(number_list))
dato_ingresado = input(f"Aqui ingreso datos ")
print(dato_ingresado)
print(f"El seno de 3 * pi es {sin(pi*3)} ")
print(f"El coseno de 3 * pi es {cos(pi*3)} ")
print(f"El tangente de 3 * pi es {tan(pi*3)} ")
print(f"Pi vale {pi}")
print(f"Este es un numero random entero entre {a} y {b} el numero es {random.randint(a,b)}")
print(f"Este es un numero random flotante entre {a} y {b} el numero es {random.uniform(a,b)}")
print(f"Esta es una eleccion de un objeto de forma random, el numero elegido es: {random.choice(number_list)}")
print("El dia de hoy es ", datetime.datetime.now())

#Now some strings functions and methods

greeting = "hello"
question = "asombroso"
long_string = "hola como te encuentras, este es un mensaje de prueba"
characters = "a b c d e f g"
characters_nospaces = "abcdefg"
delimiter = ","
delimiter_space = " "
phrase = "Los patos vuelan"
new_phrase = ""

names_list = ["Andres", " Hola", "Como te encuentras?"]

print(greeting.capitalize())
print(question.count('o'))
print(long_string.find("mensaje"))
print(characters.split())
print(delimiter.join(characters_nospaces))
print(delimiter_space.join(names_list))
print(f"Antigua frase {phrase}")
new_phrase = phrase.replace("vuelan","nadan")
print(f"Nueva frase {new_phrase}")

first_word = "Hola"
second_word = "hola"

print(first_word.casefold() == second_word.casefold())
