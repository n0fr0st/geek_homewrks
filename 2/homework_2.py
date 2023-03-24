import random

def nearest_value(num_list, value):
    abs_list = list(map(lambda num: abs(num - value), num_list))
    return num_list[abs_list.index(min(abs_list))]      

lengthN = int(input('lengthn - '))
num = int(input('num - '))
num_list = list()
for i in range(lengthN):
    num_list.append(random.randrange(1, 10))
print(num_list)
print(nearest_value(num_list, num))

