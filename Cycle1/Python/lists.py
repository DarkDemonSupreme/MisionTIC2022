from itertools import count


x = list(range(2,20,2))
print(x)

boolean_list = [False, True, False, True, True, False, True]

counter_true = 0
counter_false = 0
for i in boolean_list:
    if i == True:
        counter_true += 1
    else:
        counter_false += 1

print(counter_true)
print(counter_false)