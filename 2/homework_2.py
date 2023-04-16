import random
def arr_add():
    res_list = list()
    flag = True
    while flag == True:
        x = int(random.randrange(-20, 30))
        res_list.append(x)
        if len(res_list) > 10:
            flag = False
    print(res_list)
    return res_list

def arr_check(x, y, coll):
    list1 = list()
    for i in coll:
        if i >= x and i <= y:
            list1.append(coll.index(i))
    return list1

print(arr_check(6, 12, arr_add()))