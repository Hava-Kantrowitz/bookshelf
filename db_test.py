import sqlite3

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)

def get_table_vals():
    bookshelf_table = """ CREATE TABLE IF NOT EXISTS bookshelf (
                            id integer PRIMARY KEY,
                            title text NOT NULL,
                            author text NOT NULL
                        ),"""

def create_table(conn):
    table_set = get_table_vals()
    cont = conn.cursor()
    cont.execute(table_set)

if __name__ == '__main__':
    create_connection(r"testsqlite.db")
