from datetime import datetime

from flask import Flask, render_template, flash, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ce88b6999020eb604e7cdb913cf925e1324812ff'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )
    image_file = db.Column(
        db.String(20),
        nullable=False,
        default='default.png'
    )
    password = db.Column(
        db.String(60),
        nullable=False
    )
    posts = db.relationship(
        'Post',
        backref='author',
        lazy=True
    )

    def __repr__(self):
        return f'User("{self.username}", "{self.email}", "{self.image_file}")'


class Post(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    title = db.Column(
        db.String(100),
        nullable=False
    )
    date_posted = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow  # give the function as argument
    )
    content = db.Column(
        db.Text,
        nullable=False
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    def __repr__(self):
        return f'Post("{self.title}", "{self.date_posted}")'


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


if __name__ == '__main__':
    app.run(debug=True)
