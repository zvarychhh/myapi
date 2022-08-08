from src import api
from src.resources.books import BookListAPI

api.add_resource(BookListAPI, '/books', '/books/<uuid>', strict_slashes=False)
