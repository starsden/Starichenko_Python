import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Форма ввода адреса")

# Основной фрейм для содержимого
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

# Поле "Регион"
region_label = ttk.Label(main_frame, text="Регион")
region_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))

region_combobox = ttk.Combobox(main_frame, values=["[ не выбрано ]"], state="readonly")
region_combobox.grid(row=1, column=0, sticky=tk.EW, pady=(0, 10))
region_combobox.set("[ не выбрано ]")

# Поле "Район"
district_label = ttk.Label(main_frame, text="Район")
district_label.grid(row=2, column=0, sticky=tk.W, pady=(0, 5))

district_combobox = ttk.Combobox(main_frame, values=["Выберите район"], state="readonly")
district_combobox.grid(row=3, column=0, sticky=tk.EW, pady=(0, 10))
district_combobox.set("Выберите район")

# Поле "Город"
city_label = ttk.Label(main_frame, text="Город")
city_label.grid(row=4, column=0, sticky=tk.W, pady=(0, 5))

city_combobox = ttk.Combobox(main_frame, values=["Выберите город"], state="readonly")
city_combobox.grid(row=5, column=0, sticky=tk.EW, pady=(0, 10))
city_combobox.set("Выберите город")

# Поле "Улица"
street_label = ttk.Label(main_frame, text="Улица")
street_label.grid(row=6, column=0, sticky=tk.W, pady=(0, 5))

street_combobox = ttk.Combobox(main_frame, values=["Выберите улицу"], state="readonly")
street_combobox.grid(row=7, column=0, sticky=tk.EW, pady=(0, 10))
street_combobox.set("Выберите улицу")

# Разделительная линия
separator = ttk.Separator(main_frame, orient=tk.HORIZONTAL)
separator.grid(row=8, column=0, sticky=tk.EW, pady=10)

# Поля "Дом" и "Корпус"
house_frame = ttk.Frame(main_frame)
house_frame.grid(row=9, column=0, sticky=tk.EW, pady=(0, 10))

house_label = ttk.Label(house_frame, text="Дом")
house_label.pack(side=tk.LEFT, padx=(0, 10))

house_entry = ttk.Entry(house_frame, width=10)
house_entry.pack(side=tk.LEFT, padx=(0, 20))

building_label = ttk.Label(house_frame, text="Корпус")
building_label.pack(side=tk.LEFT, padx=(0, 10))

building_entry = ttk.Entry(house_frame, width=10)
building_entry.pack(side=tk.LEFT)

# Поля "Стр./Вл." и "Кв./Офис"
building_part_frame = ttk.Frame(main_frame)
building_part_frame.grid(row=10, column=0, sticky=tk.EW, pady=(0, 20))

building_part_label = ttk.Label(building_part_frame, text="Стр./Вл.")
building_part_label.pack(side=tk.LEFT, padx=(0, 10))

building_part_entry = ttk.Entry(building_part_frame, width=10)
building_part_entry.pack(side=tk.LEFT, padx=(0, 20))

apartment_label = ttk.Label(building_part_frame, text="Кв./Офис")
apartment_label.pack(side=tk.LEFT, padx=(0, 10))

apartment_entry = ttk.Entry(building_part_frame, width=10)
apartment_entry.pack(side=tk.LEFT)

# Кнопки "OK" и "ОТМЕНА"
buttons_frame = ttk.Frame(main_frame)
buttons_frame.grid(row=11, column=0, sticky=tk.E, pady=(10, 0))

ok_button = ttk.Button(buttons_frame, text="OK")
ok_button.pack(side=tk.LEFT, padx=(0, 10))

cancel_button = ttk.Button(buttons_frame, text="ОТМЕНА")
cancel_button.pack(side=tk.LEFT)

root.mainloop()
