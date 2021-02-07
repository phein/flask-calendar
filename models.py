import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath(__file__))

def create_post(date, fname, lname, email):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into schedules (dateNum, fname, lname, email) values(?, ?, ?, ?)', (date, fname, lname, email))
    con.commit()
    con.close()

def get_reserveList(date):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    date_query = '"' + str(date) + '"'
    cur.execute('SELECT * FROM schedules WHERE datenum=' + date_query)
    reserveList = cur.fetchall()
    return reserveList