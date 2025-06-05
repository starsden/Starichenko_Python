"""
Дано целое число в диапазоне 1-7. Вывести строку — название дня недели,
соответствующее данному числу (1 — «понедельник», 2 — «вторник" и т.д)
"""


while True:
    try:
        num = int(input("Введите целое число от 1-7: "))
        if num == 1:
            print("Понедельник")
        elif num == 2:
            print("Вторник")
        elif num == 3:
            print("Среда")
        elif num == 4:
            print("Четверг")
        elif num == 5:
            print("Пятница")
        elif num == 6:
            print("Суббота")
        elif num == 7:
            print("Воскресенье")
        else:
            print("Неверное значение")
        break

    except ValueError:
        print("Неверное значение")