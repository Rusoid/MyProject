def drink_me(param):
    msg = 'Выпиваем ' + param + ' стакан'
    print(msg)
    param = 'пустой'    

glass = 'полный'
drink_me(glass)
print('Стакан', glass)
