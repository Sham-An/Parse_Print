import sqlite3

def main():
    #При подключении к базе, автоматически создается realty.db
    connection = sqlite3.connect('realty.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE offers (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            url text,
            offer_id integer,
            date text,
            price integer,
            address text,
            area integer,
            rooms text,
            floor integer,
            total_floor
        )     
    """)
    connection.close()


if __name__ == '__main__':
    main()
