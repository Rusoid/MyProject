birthdays = {'Алиса': 'Апр 1', 'Боб': 'Дек 12', 'Кэрол': 'Мар 4'}

while True:
    print('Введите имя (<Enter> для выхода):')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(name + ': день рождения - ' + birthdays[name])
    else:
        print('Я не знаю, когда день рождения у ' + name)
        print('Когда день рождения у этого человека?')
        bday = input()
        birthdays[name] = bday
        print('Обновлена информация о дннях рождения.')
        