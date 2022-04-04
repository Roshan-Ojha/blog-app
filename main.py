from flask import Flask,render_template,request,redirect
from home import second
from about_us import about_blueprint
from register import register_blueprint
from add_detail import add
from login import check_detail,log,loggedout,blog_post,save_post

app=Flask(__name__)
app.register_blueprint(second)
app.register_blueprint(about_blueprint)
app.register_blueprint(register_blueprint)
app.register_blueprint(add)
app.register_blueprint(log)
app.register_blueprint(loggedout)
app.register_blueprint(blog_post)
app.register_blueprint(save_post)
app.secret_key='roshan'

app.register_blueprint(check_detail)





@app.route('/')
def main():
    return "<h1>Hello World!</h1>"

if __name__=='__main__':
    app.run(debug=True)