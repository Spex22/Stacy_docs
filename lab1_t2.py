import datetime

n = int(input('Количество учеников в классе:  '))
print('Формат ввода списка учеников: вводим по порядку имя, пол, г.р., рост, вес; каждое значение с новой строки')
print('ВВод списка класса: ')
klass = [[str(input()) for j in range(5)] for i in range(n)]
print('Список класса: ' + str(klass))

#Обьявление переменных
cur_year = datetime.datetime.now()
year = cur_year.year
list_weight = []
list_age = []
Sumb = 0
Sumg = 0
Avrb = 0
Avrg = 0
Growthmax = 0
Growthmin = 0
weight = 0
age = 0

#Поиск максимального веса и минимального возраста учеников
for i in range(n):
    list_age.append(year - int(klass[i][2]))
    list_weight.append(klass[i][4])
print('Список возраста' + str(list_age))
print('Список веса' + str(list_weight))
a = min(list_age)
w = max(list_weight)
print('Минимальный возраст ' + str(a))
print('Максимальный вес ' + str(w))

#Определений мах и мин значений по критериям
for i in range(n):
    if str(klass[i][1]) == 'м':
        Sumb += 1
        Avrb += (year-int(klass[i][2]))
#        print(klass[i][1]
        if int(klass[i][3]) > Growthmax:                    #Поиск мах по росту
            Growthmax = int(klass[i][3])
            weight = klass[i][4]
        elif int(klass[i][3]) == Growthmax and weight < klass[i][4]:
            Growthmax = int(klass[i][3])
            weight = klass[i][4]

    elif str(klass[i][1]) == 'ж':                           #Поиск мин по возрасту
        Sumg += 1
        Avrg += (year - int(klass[i][2]))
#        print(klass[i][1])
        if Growthmin == 0:
            Growthmin = int(klass[i][3])
            age = (year-int(klass[i][2]))
        elif Growthmin > int(klass[i][3]):
            Growthmin = int(klass[i][3])
            age = (year - int(klass[i][2]))
        elif Growthmin == int(klass[i][3]) and age > (year - int(klass[i][2])):
            Growthmin = int(klass[i][3])
            age = (year - int(klass[i][2]))

    else:
        print('Некоретные данные')
    i += 1

print('Количество мальчиков: ' + str(Sumb))
print('Количество девочек: ' + str(Sumg))
print('Средний возраст мальчиков: ' + str(Avrb/Sumb))
print('Средний возраст девочек: ' + str(Avrg/Sumg))
print('Максимальный рост мальчика: ' + str(Growthmax))
print('Минимальный рост девочки: ' + str(Growthmin))

if weight == w:
    print('Cамый высокий мальчик весит больше всех в классе')
else:
    print('Cамый высокий мальчик не весит больше всех в классе')

if age == a:
    print('Cамая маленькая девочка является самой юной среди девочек')
else:
    print('Cамая маленькая девочка не является самой юной среди девочек')
