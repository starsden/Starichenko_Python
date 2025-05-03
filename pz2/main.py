num = 10119
temp = num
digits = []

while temp > 0:
    digits.append(temp % 10)
    temp //= 10
digits.reverse()
print(digits)

for d in digits:
    print(d * d)



numbers = [2, 3, 10, 5]
result = 0
for n in numbers:
    sq = n * n
    temp = sq
    digits = []
    if temp == 0:
        digits.append(0)
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    for d in reversed(digits):
        result = result * 10 + d
print(result)





numbers = [2, 12, 22, 32, 42, 52, 62, 102, 112, 122, 132]
count = 0
for n in numbers:
    if n % 4 == 0 and n % 10 == 2:
        count += 1

print("Чисел, кратных 4 и оканчивающихся на 2:", count)
