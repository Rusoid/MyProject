def get_attributes(query, default):
    question = query + ' [' + default + ']? '
    answer = input(question)
    if (answer == ''):
        answer = default
    print('Вы выбрали', answer)
    return answer

hair = get_attributes('Цвет волос', 'темные')
hair_length = get_attributes('Длина волос', 'короткие')
eye = get_attributes('Цвет глаз', 'голубые')
gender = get_attributes('Пол', 'женский')
glasses = get_attributes('Носит очки', 'нет')
beard = get_attributes('Носит бороду', 'нет')
