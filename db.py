import sqlite3
import os.path
# from sqlite3 import Error



class Data():
    def __init__(self):
        if not os.path.exists('data/file.db'):
            self.conn = sqlite3.connect('data/file.db')
            self.c = self.conn.cursor()
            self.create_table()
        else:
            print("runn")
            self.conn = sqlite3.connect('data/file.db')
            self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute('''CREATE TABLE file 
        ( id INTIGER PRIMARY KEY, 
            name TEXT, 
            size REAL, 
            path TEXT, 
            URL  TEXT )
        
        ''')
        self.conn.commit()
        print("Table Created")
