import re
 
strValue = input('Введите слово - ').upper()
charValue = {'[AEIOULNSTR]': '1','[АВЕИНОРСТ]': '1', '[DG]': '2', '[ДКЛМПУ]': '2', '[BCMP]': '3', '[БГЁЬЯ]': '3', '[FHVWY]': '4',
             '[ЙЫ]': '4', 'K': '5', '[ЖЗХЦЧ]': '5', '[JX]': '8', '[ШЭЮ]': '8', '[QZ]': '10', '[ФЩЪ]': '10'}
for i in charValue:
    strValue = re.sub(i, charValue[i], strValue)
print(sum(map(int, strValue)))