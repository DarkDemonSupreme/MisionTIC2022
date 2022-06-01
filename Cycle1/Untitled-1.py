def calculate_final_price(price):
    return price * 1.19

for i in range(10):
    price = float(input(f"Ingrese el valor del producto {i + 1} "))
    final_price = calculate_final_price(price)
    print(f"El precio final del producto {i + 1} es {final_price}")
