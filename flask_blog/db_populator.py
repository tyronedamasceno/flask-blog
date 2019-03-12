import random

from faker import Faker

from flask_blog import db
from flask_blog.models import User, Post

fake = Faker()

for i in range(10):
    author_user = random.choice(User.query.all())
    title = fake.sentence()
    content = ' '.join(fake.paragraphs(3))
    p = Post(user_id=author_user.id, title=title, content=content)
    db.session.add(p)

db.session.commit()
