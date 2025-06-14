"""
Даны три словаря на три элемента каждый. Объединить все словари в один. Вывести исходные словари и результирующий.
"""

import tkinter as tk

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


def tl():
    word = entry.get().lower()
    translation = slova.get(word)
    if translation:
        res.config(text=f"перевод: {translation}")
    else:
        res.config(text="слова нет")


window = tk.Tk()
window.title("27 вариант 9 работы")

label = tk.Label(window, text="введите английское слово:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="перевести", command=tl)
button.pack()

res = tk.Label(window, text="")
res.pack()

window.mainloop()
