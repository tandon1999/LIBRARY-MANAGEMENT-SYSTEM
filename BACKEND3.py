import sqlite3

def connect():
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS customer(id INTEGER PRIMARY KEY,cus_id INTEGER , cus_name text,address text,city text,state text,phone_no INTEGER,a_paid INTEGER,no_books INTEGER)")
    conn.commit()
    conn.close()

def insert(cus_id,cus_name,address,city,state,phone_no,a_paid,no_books):
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO customer VALUES (NULL,?,?,?,?,?,?,?,?)",(cus_id,cus_name,address,city,state,phone_no,a_paid,no_books))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM customer")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(cus_id="",cus_name="",address="",city="",state="",phone_no="",a_paid="",no_books=""):
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM customer WHERE cus_id=? OR cus_name=? OR address=? OR city=? OR state=? OR phone_no=? OR a_paid=? OR no_books=? ", (cus_id,cus_name,address,city,state,phone_no,a_paid,no_books))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM customer WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,cus_id,cus_name,address,city,state,phone_no,a_paid,no_books):
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("UPDATE customer SET cus_id=?, cus_name=?, address=?, city=?, state=?, phone_no=?, a_paid=?, no_books=? WHERE id=?",(cus_id,cus_name,address,city,state,phone_no,a_paid,no_books,id))
    conn.commit()
    conn.close()

def total():
    conn=sqlite3.connect("bk2.db")
    cur=conn.cursor()
    cur.execute("SELECT sum(no_books) FROM customer")
    rows=cur.fetchall()
    val=int(str(rows[0]).strip('(),'))
    return val
    conn.close()


    
connect()