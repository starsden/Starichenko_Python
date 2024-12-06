while True:
    try:
        n = int(input("Введите количество секунд с начала суток: "))
        minuti = (n % 3600) // 60
        print("Количество полных минут с начала последнего часа:", minuti)
        break
    except ValueError:
        print("Неверное значение")
