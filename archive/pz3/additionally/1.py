"""
Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2
"""
while True:
    try:
        a = int(input("Введите 1 число: "))
        b = int(input("Введите 2 число: "))

        if a + b == 5:
            print(5 + 1)
        else:
            print(5 - 2)
        break

    except ValueError:
        print('Введите число!!!')
