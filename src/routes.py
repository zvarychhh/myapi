from flask import request
from flask_restful import Resource

from src import api, db
from src.models import Book


class BookListAPI(Resource):
    def get(self, uuid=None):
        if not uuid:
            books = db.session.query(Book).all()
            return [book.to_dict() for book in books], 200
        book = db.session.query(Book).filter_by(uuid=uuid).first()
        if not book:
            return '', 404
        return book.to_dict(), 200

    def post(self):
        book_json = request.json
        if not book_json:
            return {'message': 'Wrong data'}, 400
        try:
            book = Book(
                title=book_json['title'],
                author=book_json['author'],
                price=book_json['price'],
                ratting=book_json['ratting']
            )
            db.session.add(book)
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Created successfully'}, 201

    def put(self, uuid):
        book_json = request.json
        if not book_json:
            return {'message': 'Wrong data'}, 400
        try:
            db.session.query(Book).filter_by(uuid=uuid).update(
                dict(
                    title=book_json['title'],
                    author=book_json['author'],
                    price=book_json['price'],
                    ratting=book_json['ratting']
                )
            )
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Updated successfully'}, 200

    def patch(self, uuid):
        book = db.session.query(Book).filter_by(uuid=uuid).first()
        if not book:
            return '', 404
        book_json = request.json
        title = book_json.get('title')
        author = book_json.get('author'),
        price = book_json.get('price'),
        ratting = book_json.get('ratting')

        if title:
            book.title = title
        elif author:
            book.author = author
        elif price:
            book.author = price
        elif ratting:
            book.author = ratting

        db.session.add(book)
        db.session.commit()
        return {'message': 'Updated successfully'}, 200

    def delete(self, uuid):
        book = db.session.query(Book).filter_by(uuid=uuid).first()
        if not book:
            return '', 404
        db.session.delete(book)
        db.session.commit()
        return '', 204


api.add_resource(BookListAPI, '/books', '/books/<uuid>', strict_slashes=False)
