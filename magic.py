import random
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай", 
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет", "Никаких сомнений",
           "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет", "Можешь быть уверен в этом",
           "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
print('Добро пожаловать!')
print('Я - магический шар и могу предсказать твоё будущее.')
name = input('Скажи мне своё имя?')
print('Приветствую тебя,', name + '!') 
while True:
    ask = input('Введи свой вопрос:')
    print('Ответ:')
    print(random.choice(answers))
    ask2 = input('Хочешь задать еще вопрос?')
    if ask2 == 'нет':
        print('Возвращайся, если будут вопросы')
        break
