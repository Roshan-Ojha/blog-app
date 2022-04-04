from flask import render_template,Blueprint,session
import sqlite3
second=Blueprint('second',__name__)
@second.route('/home')
@second.route('/')
def home():
    conn1=sqlite3.connect('user.db')
    c1=conn1.cursor()
    c1.execute("SELECT * FROM blog")
    data1=c1.fetchall()
    conn1.commit()
    conn1.close()
    session['data'] = data1
    return render_template('home.html')
