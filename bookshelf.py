import sqlite3
from sqlite3 import Error
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('type', help="The type of action to be taken. Options are add_book, add_file, remove_book, find_book, create")
    parser.add_argument('title', nargs='?')
    parser.add_argument('author', nargs='?')
    return parser.parse_args()

def create_connection(db_file):
    conn = None
    try: 
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn 

def create_table(conn):
    create_table_sql = """ CREATE TABLE IF NOT EXISTS books (
                                id integer PRIMARY KEY,
                                title text NOT NULL,
                                author text NOT NULL
                            ); """
    try: 
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e: 
        print(e)

def add_book(conn, book):
    sql = ''' INSERT INTO books(title, author)
                VALUES(?,?) '''
    curr = conn.cursor()
    curr.execute(sql, book)
    conn.commit()
    return curr.lastrowid

def create_book(conn, title, author):
    if title == "NA":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
    book = (title, author)
    add_book(conn, book)
    again = input("Would you like to add another?")
    if "y" in again or "Y" in again: 
        title = "NA"
        author = "NA"
        create_book(conn, title, author)

def remove_book(conn, title, author):
    pass

def remove_all(conn):
    sql = 'DELETE FROM books'
    curr = conn.cursor()
    curr.execute(sql)
    conn.commit()

def main():
    args = parse_args()
    myType = args.type
    if len(vars(args)) > 1:
        title = args.title
        author = args.author
    else:
        title = "NA"
        author = "NA"
    database = r"mydatabase.db"
    conn = create_connection(database)
    
    with conn:
        if "create" in myType:
            create_table(conn, book)
        elif "add_book" in myType:
            create_book(conn, title, author)
        elif "remove_book" in myType:
            remove_book(conn, title, author)
        elif "remove_all" in myType:
            remove_all(conn)

main()
