import re

def stringConvert(Mystring):
    Mystring = Mystring.replace(" ", "")
    Mystring = Mystring.lower()
    Mystring_list = list(re.sub(r'[^\w\s]', '', Mystring))
    return Mystring_list

myString = input("Введите первую строку - ")
mySecString = input("Введите вторую строку - ")
myString_list = sorted(stringConvert(myString))
mySecString_list = sorted(stringConvert(mySecString))
if myString_list == mySecString_list:
    print("строки являются анаграммами.")
else:
    print("строки не являются анаграммами.")

