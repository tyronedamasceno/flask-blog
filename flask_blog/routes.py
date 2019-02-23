from flask import render_template, flash, redirect, url_for

from flask_blog import app
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def index():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (
            form.email.data == 'admin@mail.com' and
            form.password.data == 'password'
        ):
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash(
                'Login Unsucessful. Please check username and password',
                'danger'
            )
    return render_template('login.html', title='login', form=form)
