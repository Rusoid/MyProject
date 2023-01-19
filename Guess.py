color = 'синий'
guess = ''
guesses = 0

while guess != color:
    guess = input('Какой цвет я загадал? ')
    guesses = guesses + 1

if guesses == 1:
    print('Угадали! Вы сделали', guesses, 'попытку')
else:
    print('Угадали! Вы сделали', guesses, 'попытки')
