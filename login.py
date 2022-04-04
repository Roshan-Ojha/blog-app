from flask import render_template,Blueprint,request,session,flash,redirect,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import date
import sqlite3

log=Blueprint('login',__name__)
check_detail=Blueprint('check',__name__)
loggedout=Blueprint('logout1',__name__)
blog_post=Blueprint('blog',__name__)
save_post=Blueprint('save',__name__)



@log.route('/Login')
def login():
    return render_template('login.html')



# @check_detail.route('/success')
@check_detail.route('/',methods=['GET','POST'])


def check():

    email=request.form.get('mail')
    password=request.form.get('pass')
    try:

        conn1 = sqlite3.connect('user.db')
        c1 = conn1.cursor()
        c1.execute("SELECT * FROM blog")
        data1 = c1.fetchall()
        conn1.commit()
        conn1.close()


        conn=sqlite3.connect('user.db')
        c=conn.cursor()
        c.execute("""SELECT * FROM login WHERE email=:email""",
                  {
                      'email':email
                  })

        data=c.fetchall()
        conn.commit()
        conn.close()
        if (check_password_hash(data[0][2],password)==True):
            session['name']=data[0][0]
            session['email']=data[0][1]
            session['data']=data1
            session['login']=True
            return render_template('home.html')
        else:
            flash("Incorrect Password")
            return render_template('login.html')
    except:

        flash("No such email is registered")
        return render_template('login.html')

@loggedout.route('/Logout')
def logout():
    session.pop('name',None)
    session.pop('email',None)
    session.pop('login',None)
    return render_template('login.html')

@blog_post.route('/create')
def blog():
    return render_template('create.html')


@save_post.route('/create',methods=['GET','POST'])
def save():
    print(session.get('name'))
    print(date.today())
    print(request.form.get('title'))
    print(request.form.get('text'))
    try:
        connect=sqlite3.connect('user.db')
        cursor=connect.cursor()
        cursor.execute("""INSERT INTO blog VALUES(:name,:date,:title,:blog,:email)""",
                       {
                           'name':session.get('name'),
                           'date':date.today(),
                           'title':request.form.get('title'),
                           'blog':request.form.get('text'),
                           'email':session.get('email')
                       })
        cursor.execute("SELECT * FROM blog")

        connect.commit()
        connect.close()
        return render_template('home.html')
    except:
        flash("This title already exists")
        return render_template("create.html")

