# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

# Решение


def remove_exclamation_marks(s):
    cnt = s.count('!')
    s_new1 = s.replace('!', '', cnt)
    print(s_new1)

remove_exclamation_marks()

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

# Решение

def remove_last_em(s):
    if len(s) > 1 and s[-1] == '!':
        print(s[:-1])
    else:
        print(s)
    
remove_last_em('Hi!!')

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они сод ержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

# Решение

def remove_word_with_one_em(s):
   s_new2 = s.split(' ')
    for i in s_new2:
        if i.count('!') == 1:
            continue
        elif i.count('!') >= 2 or i.count('!') == 0:
            print(i, end = ' ')

remove_word_with_one_em('s')