import random

n = int(input("Введите длинну массива - "))
num = int(input("Введите искомое число - "))
res = 0
number_list = list()
for i in range(n):
    number_list.append(random.randrange(1, 10))
    if number_list[i] == num:
        res+=1
print(number_list)
print(res)

