#Basics

#How to print out information?
print("Hola Mundo")

#How to assign variables?
# name_of_variable = value
a = 5
b = 3
c = 0.0
#Variables can have different types like string,int,float,set,dictionary etc 
name = "Andres"
cost = 6.4

#How can I read input from the user?
#I can set a message inside of input to output 
input("This is a output message ")

#How to save it to a variable?
#Assigning him just like that

a = input("Insert a number")
print(a)

#Input brings all the input as string, how to know it?

print(type(a))

#How to convert that into a numeric value to make something with it?
#Just casting to a float

a = float(input("Insert another number"))

#Now the a variable is a float

print(a)
print(type(a))

#Now that value is a float, that means I can do math operations with it

#Simple aritmetics sum,difference,multiplication,division

c = a + b
print(c)
# Should be 8
d = a - b
print(d)
# Should be 2
e = a * b
print(e)
# Should be 15
f = a / b 
print(f)
# Should be 3.33


