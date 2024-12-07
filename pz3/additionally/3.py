"""
Вести число. Если оно четное, разделить его на 4, если нечетное - умножить на 5.
"""

while True:
    try:
        a = int(input("Введите число: "))
        if a % 2 == 0:
            print(a // 2)
        else:
            print(a * 5)

    except ValueError:
        print("Введите число!!!")