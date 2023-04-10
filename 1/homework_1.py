

ang = set([int(x) for x in input("vvedite chislo - ").split()])
ang_1 = set([int(x) for x in input("vvedite chislo - ").split()])
dif_Set = ang & ang_1
res_set = list(dif_Set)
res_set.sort()
for i in res_set:
    print(i, end=" ")

