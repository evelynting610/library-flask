from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy import func

from library.extensions import db
from library.mixins import CRUDMixin


class Request(CRUDMixin, db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer)
    book = db.relationship(
        'Book',
        uselist=False,
        primaryjoin='foreign(Book.id) == Request.book_id',
        passive_deletes=True)
    user_id = db.Column(db.Integer)
    requested_at = db.Column(db.DateTime, default=func.now())

    @property
    def available(self):
        return not self.book.borrower_id

    @property
    def title(self):
        return self.book.title


class Book(CRUDMixin, db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(TEXT, index=True)
    borrower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    borrower = db.relationship('User', back_populates='borrowed_books')
    user_requests = db.relationship(
        'Request',
        primaryjoin='foreign(Request.book_id) == Book.id',
        order_by='asc(Request.requested_at)')
    date_due = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())


class User(CRUDMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(TEXT)
    email = db.Column(TEXT)
    book_requests = db.relationship('Request', primaryjoin='foreign(Request.user_id) == User.id')
    borrowed_books = db.relationship('Book', back_populates='borrower')
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())
