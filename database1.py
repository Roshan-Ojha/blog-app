import sqlite3
conn=sqlite3.connect('user.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS login(
            name text,
            email text UNIQUE ,
            password text
            )""")
c.execute("""CREATE TABLE IF NOT EXISTS blog(
            name text,
            date text,
            title text UNIQUE ,
            blog text,
            email text
            )""")

conn.commit()
conn.close()