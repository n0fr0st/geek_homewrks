n = int(input())
kust_list = list()
for i in range(n):
    x = int(input())
    kust_list.append(x)

res_list = list()
for i in range(len(kust_list)-1):
    res_list.append(kust_list[i-1] + kust_list[i] + kust_list[i+1])
res_list.append(kust_list[-2] + kust_list[-1] + kust_list[0])
print(max(res_list))