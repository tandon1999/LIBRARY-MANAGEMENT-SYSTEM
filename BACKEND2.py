import sqlite3

def connect():
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book_p (id INTEGER PRIMARY KEY, title text, author text, quantity INTEGER, price INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,quantity,price):
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book_p VALUES (NULL,?,?,?,?)",(title,author,quantity,price))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book_p")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",quantity="",price=""):
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book_p WHERE title=? OR author=? OR quantity=? OR price=?", (title,author,quantity,price))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book_p WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,quantity,price):
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("UPDATE book_p SET title=?, author=?, quantity=?, price=? WHERE id=?",(title,author,quantity,price,id))
    conn.commit()
    conn.close()

def total():
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("SELECT sum(quantity) FROM book_p")
    rows=cur.fetchall()
    val=int(str(rows[0]).strip('(),'))
    return val
    conn.close()
    
def maxval():
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("SELECT max(price) FROM book_p")
    rows=cur.fetchall()
    val=int(str(rows[0]).strip('(),'))
    return val
    conn.close()

def minval():
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("SELECT min(price) FROM book_p")
    rows=cur.fetchall()
    val=int(str(rows[0]).strip('(),'))
    return val
    conn.close()
    
connect()





