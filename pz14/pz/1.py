'''
В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и ДД/ММ/ГГГГ.
Посчитать количество дат в каждом формате. Поместить в новый текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.
'''

import re

file = open('dates.txt', "r")
text = file.read()
file.close()

per = re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", text)
vtor = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)

fevrals = []
for date in vtor:
    if '/02/' in date:
        fevrals.append(date)

print(f"дд.мм.гггг: {len(per)}")
print(f"дд/мм/гггг: {len(vtor)}")

res = open("result.txt", "w", encoding="utf-8")
for date in fevrals:
    res.write(date + "\n")
res.close()