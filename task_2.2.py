# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.


def quarter_of(month):
    month_list = ('январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')
    if month >= 1 and month <= 3:
        result = 'Месяц ' + str(month) + ' - ' + str(month_list[month-1]) + '. Является частью первого квартала.'
    elif month > 3 and n < 7:
        result = 'Месяц ' + str(month) + ' - ' + str(month_list[month-1]) + '. Является частью второго квартала.'
    elif month > 6 and n < 10:
        result = 'Месяц ' + str(month) + ' - ' + str(month_list[month-1]) + '. Является частью третьего квартала.'
    elif month > 9 and n < 13:
        result = 'Месяц ' + str(month) + ' - ' + str(month_list[month-1]) + '. Является частью четвертого квартала.'
    else: 
        result = 'Такого месяца не существует'
    return result

print(quarter_of())
