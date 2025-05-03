"""
Органзовать словарь на 10 англо-русских слов, обеспечивающий "Перевод" английского слова на русский
"""

slova = {
    "apple": "яблоко",
    "dog": "собака",
    "sun": "солнце",
    "water": "вода",
    "book": "книга",
    "house": "дом",
    "friend": "друг",
    "car": "машина",
    "tree": "дерево",
    "computer": "компьютер"
}

word = input("Введите английское слово: ").strip().lower()

try:
    translate = slova[word]
    print("Перевод:", translate)

except KeyError:
    print("слова нет")