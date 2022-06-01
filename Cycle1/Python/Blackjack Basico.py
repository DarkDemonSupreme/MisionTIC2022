#Realizar un blackjack
#Realizar un programa que detecte un doble
import random

is_delivered = False
taken_card = False
sum_cards = 0
dealer_sum_cards = 0
number_cards = 0

print("Bienvenido al blackjack!")
print("A continuación le van a repartir dos cartas")
print("Debe elegir que desea hacer")
print("Recuerde que si se pasa de 21, pierde")

while not is_delivered:

    for i in range(2):
        i = random.randint(1,11)
        sum_cards += i
        print(f"Sus cartas son: {i}")
        print(f"{i} es la carta")

    for i in range(1):
        i = random.randint(1,11)
        dealer_sum_cards += i
        number_cards += 1
        print(f"La {number_cards} carta del dealer es {i}")

    print(f"La suma de sus cartas es: {sum_cards}")
    print("Desea quedarse o quiere pedir?")
    
    while not taken_card:
        option = int(input("Presione 2 para pedir o 0 para quedarse "))
        if option == 2:
            for i in range(1):
                i = random.randint(1,11)
                print(f"La carta que te salio fue {i} ")
                sum_cards += i
                print(f"La suma de sus cartas es: {sum_cards}")
        else:
            taken_card = True
            for i in range(1):
                i = random.randint(1,11)
                dealer_sum_cards += i
                number_cards += 1
                print(f"La segunda carta del dealer es {i}")

            while dealer_sum_cards < 21:              
                print(f"El dealer ha pedido carta")
                for i in range(1):
                    i = random.randint(1,11)
                    dealer_sum_cards += i
                    number_cards += 1
                    print(f"La {number_cards} carta del dealer es {i}")
                    print(f"La suma de las cartas del dealer es {dealer_sum_cards}")
                if dealer_sum_cards > sum_cards and dealer_sum_cards < 21:
                    print(f"El dealer dejo de pedir")
                    print(f"El dealer ha ganado")
                    break
                
        if dealer_sum_cards > 21:
            print("Has ganado")
            break
                
        if sum_cards == 21:
            print("Has ganado!")
            break
        elif sum_cards > 21:
            print("Te pasaste, has perdido")
            taken_card = True
    
    is_delivered = True