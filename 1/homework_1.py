import re

def resarr(coll, d):
    res = list()
    for x in coll:
        for key in d:
            x = re.sub(key, d[key], x)
        res.append(sum(map(int, x)))
    return res

def resAnsw(coll):
    if [i for i in coll if i !=coll[0]]==[]: 
        print("Парам пам-пам")
    else:
        print("Пам парам")


mystr = input()
strArr = list(mystr.split(" "))
numArr = list()
d = { '[уеыаоэяию]':'1','[йцкнгшщзхфвпрлджчсмтб-]':'0'}
numArr = resarr(strArr, d)
resAnsw(numArr)







