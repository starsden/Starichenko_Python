n = int(input("Введите количество секунд с начала суток: "))
a = n % 3600
minuti = a // 60
print("Количество полных минут с начала последнего часа:", minuti)
