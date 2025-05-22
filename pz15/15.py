import sqlite3

DB_NAME = 'internet_store.db'

def init_db(db_name=DB_NAME):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    # Создаем таблицу Продажи, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Продажи (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fio TEXT NOT NULL,
            товар TEXT NOT NULL,
            единица_измерения TEXT NOT NULL CHECK(единица_измерения IN ('штуки', 'килограммы', 'литры')),
            количество REAL NOT NULL CHECK(количество > 0),
            стоимость REAL NOT NULL CHECK(стоимость >= 0)
        );
    ''')
    conn.commit()
    conn.close()


def add_sale(fio, товар, единица, количество, стоимость, db_name=DB_NAME):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO Продажи (fio, товар, единица_измерения, количество, стоимость)
        VALUES (?, ?, ?, ?, ?);
        ''',
        (fio, товар, единица, количество, стоимость)
    )
    conn.commit()
    conn.close()

# Получение всех записей о продажах

def get_all_sales(db_name=DB_NAME):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT id, fio, товар, единица_измерения, количество, стоимость FROM Продажи;')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Пример использования

def main():
    # Инициализируем БД и таблицу
    init_db()

    # Добавим несколько записей
    add_sale('Иванов Иван Иванович', 'Яблоки', 'килограммы', 5.5, 330.0)
    add_sale('Петров Петр Петрович', 'Бутылка воды', 'литры', 2, 60.0)
    add_sale('Сидорова Анна Сергеевна', 'Батарейки', 'штуки', 10, 150.0)

    # Выведем все продажи
    sales = get_all_sales()
    print("Все продажи:")
    for sale in sales:
        print(f"ID: {sale[0]}, ФИО: {sale[1]}, Товар: {sale[2]}, \"{sale[3]}\", Кол-во: {sale[4]}, Стоимость: {sale[5]}")

if __name__ == '__main__':
    main()