import sqlite3 as sq

with sq.connect('clients.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS clients
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                fio TEXT NOT NULL,
                percen INT NOT NULL,
                srok INT NOT NULL);""")

    data = [
        ['Стариченко Денис Евгеньевич', '5', '100'],
        ['Шакулин Аристарх Андреевич', '4', '200'],
        ['Чубенко Алина Сергеевна', '3', '300']
    ]
    cur.executemany("INSERT INTO clients (fio, percen, srok) VALUES (?, ?, ?)",data)
    con.commit()

cur.execute("DELETE FROM clients WHERE id = ?", (2,))
con.commit()