import sqlite3 as sq

with sq.connect('store.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS sales
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                fio TEXT NOT NULL,
                tovar TEXT NOT NULL,
                unit VARCHAR(10) NOT NULL,
                quantity INTEGER NOT NULL,
                price INTEGER NOT NULL);""")

    data = [
        ['Стариченко Денис Евгеньевич', 'Шаурма с курицей', 'штука', 1, 200],
        ['Кяк Денис Евгеньевич', 'Шаурма с говядиной', 'штука', 1, 250],
        ['Бам Денис Евгеньевич', 'Шаурма с ягнятиной', 'штука', 1, 300],
        ['Бим Денис Евгеньевич', 'Шаурма с щукой', 'штука', 1, 500],
        ['Бум Денис Евгеньевич', 'Шаурма со свининой', 'штука', 1, 250],
        ['Ким Денис Евгеньевич', 'Шаурма с телятиной', 'штука', 1, 290],
        ['Как Денис Евгеньевич', 'Шаурма с бараниной', 'штука', 1, 300]
    ]
    cur.executemany("INSERT INTO sales (fio, tovar, unit, quantity, price) VALUES (?, ?, ?, ?, ?)",data)
    con.commit()

    # поиск по id
    cur.execute("SELECT fio, tovar, price FROM sales WHERE id = ?", (3,))
    print(cur.fetchall())

    # поиск по ФИО
    cur.execute("SELECT * FROM sales WHERE fio = ?", ('Стариченко Денис Евгеньевич',))
    print(cur.fetchall())

    # поиск по товару
    cur.execute("SELECT * FROM sales WHERE tovar = ?", ('Шаурма с курицей',))
    print(cur.fetchall())




    # удаление по id
    cur.execute("DELETE FROM sales WHERE id = ?", (1,))
    print('удалил по id')

    # удаление по количеству
    cur.execute("DELETE FROM sales WHERE quantity = ?", (1,))
    print('удалил по кол-ву')

    # удаление по цене меньше ???
    cur.execute("DELETE FROM sales WHERE price < ?", (250,))
    print('удалил по цене')
    con.commit()





    # обновить цену по id
    cur.execute("UPDATE sales SET price = ? WHERE id = ?", (350, 2, ))
    print('обновил цену')

    # обновить количество по ФИО
    cur.execute("UPDATE sales SET quantity = ? WHERE fio = ?",(2, 'Стариченко Денис Евгеньевич'))
    print('обновил кол-во')

    # увеличить цену на 50 для товаров с ценой ниже 300
    cur.execute("UPDATE sales SET price = price + 50 WHERE price < ?", (300,))
    print('увеличил цену')
    con.commit()