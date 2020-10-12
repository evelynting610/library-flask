import click
from flask.cli import with_appcontext
from library.models import Book, User, Request
from library.models import db


@click.command()
@with_appcontext
def drop_db():
    if click.confirm('Are you sure you want to drop the db?', abort=True):
        db.drop_all()
        db.engine.execute('DROP TABLE IF EXISTS alembic_version')


@click.command('seed')
@with_appcontext
def seed():
    add_books()
    add_users()
    add_requests()
    db.session.commit()


def add_books():
    books = [
        Book(id=1, title='Infinite Jest', borrower_id=3, date_due=None),
        Book(id=2, title='The Vanishing Half', borrower_id=3, date_due=None),
        Book(id=3, title='Give and Take', borrower_id=1, date_due=None)
    ]
    for b in books:
        db.session.add(b)


def add_users():
    users = [
        User(id=1, name='Eleanor Roosevelt', email='eroosevelt@gmail.com'),
        User(id=2, name='Ariana Grande', email='agrande@gmail.com'),
        User(id=3, name='Maya Angelou', email='mangelou@gmail.com')
    ]
    for u in users:
        db.session.add(u)


def add_requests():
    requests = [
        Request(book_id=1, user_id=1),
        Request(book_id=1, user_id=2),
        Request(book_id=2, user_id=1)
    ]
    for r in requests:
        db.session.add(r)
