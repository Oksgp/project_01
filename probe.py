def get_topmgrs_list(dct_report):
    mgrs_list = []
    for name in employees.keys():
        if employees[name] >= 100000:
            mgrs_list.append(name)
    return mgrs_list
 


employees = {
    'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121
    }

top_managers = get_topmgrs_list
print(top_managers)
 
# Вариант 1
top_managers = []
for name in employees.keys():
    if employees[name] >= 100000:
        top_managers.append(name)
 
print(top_managers)
 
# Вариант 2
top_managers = [name for name, salary in employees.items() if salary >= 100000]
 
print(top_managers)

def greeting(name):
    print(f'Hello, {name}')

# Принцип DRY - Dont repeat yourself
# Создание функции
def greeting(name):
    print(f'Hello, {name}')
 
# Вызов функции
greeting('Mark')
 
# Вызов функции с параметром
for i in ['Mark', 'R2D2', 'Anakin', 'World']:
    greeting(i)