import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Форма ввода адреса")
root.geometry("400x425")

main = ttk.Frame(root, padding="10")
main.pack(fill=tk.BOTH, expand=True)

region = ttk.Label(main, text="Регион")
region.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))

regionbox = ttk.Combobox(main, values=["[ не выбрано ]"], state="readonly")
regionbox.grid(row=1, column=0, sticky=tk.EW, pady=(0, 10))
regionbox.set("[ не выбрано ]")

rayon = ttk.Label(main, text="Район")
rayon.grid(row=2, column=0, sticky=tk.W, pady=(0, 5))

rayonbox = ttk.Combobox(main, values=["Выберите район"], state="readonly")
rayonbox.grid(row=3, column=0, sticky=tk.EW, pady=(0, 10))
rayonbox.set("Выберите район")

city = ttk.Label(main, text="Город")
city.grid(row=4, column=0, sticky=tk.W, pady=(0, 5))

citybox = ttk.Combobox(main, values=["Выберите город"], state="readonly")
citybox.grid(row=5, column=0, sticky=tk.EW, pady=(0, 10))
citybox.set("Выберите город")

street = ttk.Label(main, text="Улица")
street.grid(row=6, column=0, sticky=tk.W, pady=(0, 5))

streetbox = ttk.Combobox(main, values=["Выберите улицу"], state="readonly")
streetbox.grid(row=7, column=0, sticky=tk.EW, pady=(0, 10))
streetbox.set("Выберите улицу")

sep = ttk.Separator(main, orient=tk.HORIZONTAL)
sep.grid(row=8, column=0, sticky=tk.EW, pady=10)


house = ttk.Frame(main)
house.grid(row=9, column=0, sticky=tk.EW, pady=(0, 10))

housebox = ttk.Label(house, text="Дом")
housebox.pack(side=tk.LEFT, padx=(0, 10))

houseentry = ttk.Entry(house, width=10)
houseentry.pack(side=tk.LEFT, padx=(0, 20))

korp = ttk.Label(house, text="Корпус")
korp.pack(side=tk.LEFT, padx=(0, 10))

korpent = ttk.Entry(house, width=10)
korpent.pack(side=tk.LEFT)


stroy = ttk.Frame(main)
stroy.grid(row=10, column=0, sticky=tk.EW, pady=(0, 20))

stroybox = ttk.Label(stroy, text="Стр./Вл.")
stroybox.pack(side=tk.LEFT, padx=(0, 10))

stroyent = ttk.Entry(stroy, width=10)
stroyent.pack(side=tk.LEFT, padx=(0, 20))

kvrt = ttk.Label(stroy, text="Кв./Офис")
kvrt.pack(side=tk.LEFT, padx=(0, 10))

kvrtent = ttk.Entry(stroy, width=10)
kvrtent.pack(side=tk.LEFT)

buttons_frame = ttk.Frame(main)
buttons_frame.grid(row=11, column=0, sticky=tk.E, pady=(10, 0))

ok_button = ttk.Button(buttons_frame, text="OK")
ok_button.pack(side=tk.LEFT, padx=(0, 10))

cancel_button = ttk.Button(buttons_frame, text="ОТМЕНА")
cancel_button.pack(side=tk.LEFT)

root.mainloop()
