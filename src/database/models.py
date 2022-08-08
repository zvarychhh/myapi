import uuid

from src import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), index=True, nullable=False)
    uuid = db.Column(db.String(36), unique=True)
    price = db.Column(db.FLOAT)
    ratting = db.Column(db.FLOAT)

    def __init__(self, title, author, price, ratting):
        self.title = title
        self.author = author
        self.uuid = str(uuid.uuid4())
        self.price = price
        self.ratting = ratting

    def __repr__(self):
        return f'Book({self.title}, {self.author}, {self.price}, {self.ratting})'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'uuid': self.uuid,
            'price': self.price,
            'ratting': self.ratting
        }
