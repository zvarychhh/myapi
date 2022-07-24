from flask import request
from flask_restful import Resource

from src import api


def get_all_books():
    return [{'id': '1', 'name': '1984', 'author': 'George Orwell'},
            {'id': '2', 'name': 'We Are the Brennans', 'author': 'Tracey Lange'},
            {'id': '3', 'name': 'The In Between', 'author': 'Marc Klein'},
            {'id': '4', 'name': 'The Mix-Up', 'author': 'Holly McCulloch'},
            {'id': '5', 'name': 'Sunset', 'author': 'Jessie Cave'}]
    # {'id': '6', 'name': 'test', 'author': 'test'}


def get_books_by_bid(uuid: str) -> dict:
    books = get_all_books()
    book = list(filter(lambda x: x['id'] == uuid, books))
    return book[0] if book else {}


def create_book(book_json: dict) -> list[dict]:
    books = get_all_books()
    books.append(book_json)
    return books


class BookListAPI(Resource):
    def get(self, uuid=None):
        if not uuid:
            books = get_all_books()
            return books, 200
        book = get_books_by_bid(uuid)
        if not book:
            return '', 404
        return book, 200

    def post(self):
        book_json = request.json
        return create_book(book_json), 201

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass


api.add_resource(BookListAPI, '/books', '/books/<uuid>', strict_slashes=False)
