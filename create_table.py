import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


def create_items():
    print("test1")
    create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
    cursor.execute(create_table)


def create_users():
    # MUST BE INTEGER
    # This is the only place where int vs INTEGER matters—in auto-incrementing columns
    create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
    cursor.execute(create_table)


connection.commit()
connection.close()
