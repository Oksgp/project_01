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

remove_exclamation_marks('Hi! Hello!')