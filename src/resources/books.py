from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src import db
from src.database.models import Book
from src.schemas.book import BookSchema


class BookListAPI(Resource):
    book_schema = BookSchema()

    def get(self, uuid=None):
        if not uuid:
            books = db.session.query(Book).all()
            return self.book_schema.dump(books, many=True), 200
        book = db.session.query(Book).filter_by(uuid=uuid).first()
        if not book:
            return '', 404
        return self.book_schema.dump(book), 200

    def post(self):
        try:
            book = self.book_schema.load(request.json, session=db.session)
        except (ValidationError, TypeError) as e:
            return {'message': str(e)}, 400
        db.session.add(book)
        db.session.commit()
        return self.book_schema.dump(book), 201

    def put(self, uuid):
        book = db.session.query(Book).filter_by(uuid=uuid).first()
        if not book:
            return "", 404
        try:
            book = self.book_schema.load(request.json, instance=book, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(book)
        db.session.commit()
        return self.book_schema.dump(book), 200

    def patch(self, uuid):
        book = db.session.query(Book).filter_by(uuid=uuid).first()
        if not book:
            return '', 404
        try:
            book = self.book_schema.load(request.json, instance=book, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(book)
        db.session.commit()
        return self.book_schema.dump(book), 200

    def delete(self, uuid):
        book = db.session.query(Book).filter_by(uuid=uuid).first()
        if not book:
            return '', 404
        db.session.delete(book)
        db.session.commit()
        return '', 204
