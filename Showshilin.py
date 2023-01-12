import random

winner = ' '

random_choice = random.randint(0, 2)

if random_choice == 0:
    computer_choice = 'камень'
elif random_choice == 1:
    computer_choice = 'бумага'
else:
    computer_choice = 'ножницы'

#user_choice = input('камень, ножницы или бумага? ')

user_choice = ' '
while (user_choice != 'камень' and
        user_choice != 'бумага' and
        user_choice != 'ножиницы'):
    user_choice = input('камень, ножницы или бумага? ')

if computer_choice == user_choice:
    winner = 'Ничья'
elif computer_choice == 'бумага' and user_choice == 'камень':
    winner = 'Компьютер'
elif computer_choice == 'камень' and user_choice == 'ножницы':
    winner = 'Компьютер'
elif computer_choice == 'ножницы' and user_choice == 'бумага':
    winner = 'Компьютер'
else:
    winner = 'Пользователь'

if winner == 'Ничья':
    print('Мы оба выбрали', computer_choice + ', играем снова.')
else:
    print(winner, 'выиграл, я выбрал', computer_choice + '.')
