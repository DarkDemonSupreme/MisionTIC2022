iva = 1.19
final_cost = 0
how_many_packages = 0

how_many_packages = int(input())

for i in range(how_many_packages):
    height = float(input())
    wide = float(input())
    deep = float(input())
    volume = height * wide * deep
    cost = volume * 5

    if height > 30:
        cost += 2000

    if cost > 10000:
        cost = cost * iva

    final_cost += cost
    print(volume)
    print(cost)

print(final_cost)