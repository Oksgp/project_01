# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Решение
import random
import datetime
from math import *
my_favorite_songs_values = list(dict(my_favorite_songs).values())
time_summary =  sum(random.sample(my_favorite_songs_values, k = 3))
minutes = int(floor(time_summary))
seconds = int(time_summary * 100 % 100) 
if seconds > 60:
    minutes += 1
    seconds -= 60
print('Три песни звучат', datetime.time(00, minutes, seconds).strftime('%M:%S'), 'минут')


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

values_dict = list(my_favorite_songs_dict.values())
time_sum = sum(random.sample(values_dict, k = 3))
minutes_dict = int(floor(time_sum))
seconds_dict = int(time_sum * 100 % 100)
if seconds_dict > 60:
    minutes_dict += 1
    seconds_dict -= 60 
print('Три песни звучат', datetime.time(00, minutes_dict, seconds_dict).strftime('%M:%S'), 'минут')




# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

