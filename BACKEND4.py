import sqlite3

def connect():
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookseller(id INTEGER PRIMARY KEY,booksell_id INTEGER , first_name text,middle_name text,last_name text,location text,phone_no INTEGER,revenue INTEGER)")
    conn.commit()
    conn.close()

def insert(booksell_id,first_name,middle_name,last_name,location,phone_no,revenue):
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO bookseller VALUES (NULL,?,?,?,?,?,?,?)",(booksell_id,first_name,middle_name,last_name,location,phone_no,revenue))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookseller")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(booksell_id="",first_name="",middle_name="",last_name="",location="",phone_no="",revenue=""):
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookseller WHERE booksell_id=? OR first_name=? OR middle_name=? OR last_name=? OR location=? OR phone_no=? OR revenue=?", (booksell_id,first_name,middle_name,last_name,location,phone_no,revenue))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM bookseller WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,booksell_id,first_name,middle_name,last_name,location,phone_no,revenue):
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("UPDATE bookseller SET booksell_id=?, first_name=?,middle_name=?,last_name=?,location=?,phone_no=?,revenue=? WHERE id=?",(booksell_id,first_name,middle_name,last_name,location,phone_no,revenue,id))
    conn.commit()
    conn.close()

def total():
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("SELECT count(booksell_id) FROM bookseller")
    rows=cur.fetchall()
    val=int(str(rows[0]).strip('(),'))
    return val
    conn.close()


    
connect()

