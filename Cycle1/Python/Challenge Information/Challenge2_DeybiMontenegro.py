height = float(input())
wide = float(input())
deep = float(input())
volume = height * wide * deep
cost = volume * 5
iva = 1.19

if height > 30:
    cost += 2000

if cost > 10000:
    cost = cost * iva

print(volume)
print(cost)