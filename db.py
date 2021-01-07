import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, book text, customer text, startDate text, price text)")
        self.conn.commit

    def fetch(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return rows

    def insert(self, book, customer, startDate, price):
        self.cur.execute("INSERT INTO books VALUES(NULL, ?, ?, ?, ?)", (book, customer, startDate, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM books WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, book, customer, startDate, price):
        self.cur.execute("UPDATE books SET book=?, customer=?, startDate=?, price=? WHERE id=? ",(book, customer, startDate, price, id))
        self.conn.commit()

    def _del_(self):
        self.conn.close()

db = Database('store.db')
    
