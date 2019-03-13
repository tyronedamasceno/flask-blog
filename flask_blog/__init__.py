from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_blog.config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail(app)

# import after flask app iniatilization for avoid circular imports
from flask_blog.users.routes import users as users_bp
from flask_blog.posts.routes import posts as posts_bp
from flask_blog.main.routes import main as main_bp

app.register_blueprint(users_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(main_bp)
