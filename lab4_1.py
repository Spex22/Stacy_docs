#Скопировать из файла F1 в файл F2 строки, начиная с К до К+5.
# Подсчитать количество гласных букв в F2.
from collections import Counter

k = int(input('Введите номер строки:  '))
nline = []
sum = 0

for i in range(6):
    nline.append(k)
    k += 1

print('Вывод номеров строк: ' + str(nline))

file = open('for_l4.txt')
new_file = open('for_l.txt','w')

#добавление строк с к=того элемента
for n, line in enumerate(file):
    if (n+1) in nline:
        new_file.write(line)

file.close()
new_file.close()

#Вывод содержимого файла
with open('for_l.txt', 'r') as f:
    print(f.read())
    
#gодсчет гласных в новом файле
f = open('for_l.txt','r')
counter = Counter(f.read())
print(counter)
sum = (counter['а'] + counter['о'] + counter['у'] + counter['ю'] + counter['и'] + counter['ы'] +counter['е'] + counter['э'] + counter['ё'] + counter['я'])
print(sum)
f.close()
