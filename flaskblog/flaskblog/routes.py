from flaskblog import app
from flask import render_template, url_for,flash,redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'DmV',
        'title': 'Some blog post',
        'content': 'First post'
    }, 
    {
        'author': 'DmV',
        'title': 'Some other blog post',
        'content': 'Secont post'
    }
]


@app.route('/about')
def about():
    return render_template("about.html", title = "hello")


@app.route('/')
@app.route('/home')
def homepage():
    return render_template("posts_page.html", posts = posts)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('homepage'))
    return render_template('register.html', title='Register', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form = form)