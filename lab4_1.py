#Скопировать из файла F1 в файл F2 строки, начиная с К до К+5.
# Подсчитать количество гласных букв в F2.
from collections import Counter
import collections

k = int(input('Введите номер строки:  '))
nline = []
gl = ['а','о','у','ы','и','я','е','ё','ю']
sum = 0

for i in range(6):
    nline.append(k)
    k += 1

print('Вывод номеров строк: ' + str(nline))

file = open('for_l4.txt')
new_file = open('for_l.txt','w')

for n, line in enumerate(file):
    if (n+1) in nline:
        new_file.write(line)

file.close()
new_file.close()

with open('for_l.txt', 'r') as f:
    print(f.read())



