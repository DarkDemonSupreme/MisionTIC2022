def calcularCosto(height,wide,deep):
    volume = height * wide * deep
    cost = volume * 5
    if height > 30:
        cost += 2000
    if cost > 10000:
        cost = cost * 1.19
    return cost

def costoTotal(numeroPaquetes,descuento):
    cost = 0
    for i in range(numeroPaquetes):
        height = float(input())
        wide = float(input())
        deep = float(input())
        cost += calcularCosto(height,wide,deep)
    discount_to_apply = cost*(descuento / 100)
    final_cost = cost - discount_to_apply
    return final_cost
