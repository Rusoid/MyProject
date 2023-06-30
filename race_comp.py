# Путевой компьютер

program = "Путевой компьютер, v.0.0.1"

# Переменные

stars = 80          # Количество звездочек
tabs = 5            # Количество отступов

dist = 0            # Расстояние, которое нужно проехать
speed = 0           # Средняя скорость авто, км/ч
time = 0            # Время в движении (за рулем)
total_time = 0      # Общее количество времени в пути

tank = 0            # Размер бака
consum = 0          # Средний расход л/100 км
dist = 0            # Расстояние в км
refuels = 0         # Количество дозаправок
refuel_time = 0     # Время дозаправки
fuel = 0            # Сколько затрачено топлива
price = 0

breaks = 0          # Количество плановых остановок
break_time = 0      # Время каждой плановой остановки

# Выводим заголовок
print("\t" * tabs, program)
print("*" * stars)

# Ввод данных от пользователей
dist = int(input("Введите расстояниеб км: "))
speed = int(input("Планируемая средняя скорость (целое число): "))
consum = float(input("Введите средний расход л./100 км: "))
tank = float(input("Объем бака, л: "))
price = float(input("Стоимость 1 литра топлива, р: "))
breaks = float(input("Количество плановых остановок (без дозаправок): "))
break_time = float(input("Время каждой плановой остановки, минут: "))

# Производим вычисления
time = dist * 60 / speed        # Время за рулем
fuel = consum * dist / 100      # Всего затрачено топлива

refuels = fuel // tank
total_time = time + refuels * refuel_time + breaks * break_time
refuel_time = breaks * break_time

print("*" * stars)
print("\t" * tabs, "Результаты:")

print("Время за рулем, ч: ", time / 60)
print("Общее время в пути, ч: ", total_time / 60)
print("Количество дозаправок: ", refuels)
print("Потрачено времени на дозаправку: ", refuels * refuel_time, " минут")
print("Израсходовано топлива, л.: ", fuel)
print("Стоимость топлива, р: ", fuel * price)

