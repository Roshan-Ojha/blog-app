from flask import render_template, Blueprint,url_for,request,flash,session
from werkzeug.security import generate_password_hash,check_password_hash

import sqlite3
add=Blueprint('add_detail',__name__)



@add.route('/succesfull')
@add.route('/login',methods=['GET','POST'])
def home1():
    name=request.form.get('name')
    email=request.form.get('mail')
    pass1=request.form.get('pass1')
    pass2=request.form.get('pass2')
    p1=generate_password_hash(pass1)
    check=check_password_hash(p1,pass2)
    if check == True:
        try:
            conn=sqlite3.connect('user.db')
            c=conn.cursor()
            c.execute("""INSERT INTO login VALUES (:name,:email,:password)""",
                      {
                          'name':name,
                          'email':email,
                          'password':p1
                      })

            conn.commit()
            conn.close()

            return render_template('login.html')
        except:
            flash("Email already exists.")
            return render_template('register.html')
    else:
        return render_template('register.html')