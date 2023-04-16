x = int(input())
y = int(input())
z = int(input())

def arrfunc(x, y, z):
    res_list = list()
    for i in range(z):
        res_list.append(x)
        x = x + y
    return res_list

print(arrfunc(x, y, z))
    