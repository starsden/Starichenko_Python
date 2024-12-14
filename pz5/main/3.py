"""
Написать программу, подсчитывающую количество цифр числа, используя для
этого функцию.
"""

while True:
    try:
        def cow(a):
            return len(str(abs(a)))

        num = int(input("Введите число: "))
        d = cow(num)
        print(f"Количество цифр: {d}")

    except ValueError:
        print("Введите число!!!")