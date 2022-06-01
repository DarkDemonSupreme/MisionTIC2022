from random import randint


tuple1 = (23,11,32,44,22)
tuple2 = (range(2,11,2))

final_list = []

max_len = len(tuple1)
print(max_len)
for i in range(max_len):
    final_list.append(tuple1[i])
    final_list.append(tuple2[i])

print(final_list)

a = tuple(range(1, 10, 2))
b = tuple(range(2, 11, 2))
print(a)
print(b)
c = list(a)
print(c)
tam = len(b)
for i in range(tam):
    posicion = 2*i+1
    c.insert(posicion, b[i])
print(c)
