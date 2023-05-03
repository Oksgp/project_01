# Угадайка)

import random
rand_number = random.randint(1, 100)
print(rand_number)
print('Добро пожаловать в числовую угадайку!')

n = input('Введите целое число от 1 до 100')

def is_valid(number):
    if number.isdigit():
        if int(number) >= 1 and int(number) <= 100:
            return True
        else:
            return False
    else:
        return False

while True:    
    if is_valid(n) == True:
        if int(n) > rand_number:
            print('много')
            n = input('Введите целое число от 1 до 100')
        elif int(n) < rand_number:
            print('мало')
            n = input('Введите целое число от 1 до 100')
        elif int(n) == rand_number:
            print('угадал')
            break
    elif is_valid(n) == False:
        print('А может все-таки целое число от 1 до 100?')
        n = input('Введите целое число от 1 до 100')
