from flask import render_template, request, Blueprint
from flask_blog.models import Post


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/index")
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(
        page=page, per_page=5
    )
    return render_template('index.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
