from src import db
from src.models import Book


def populate_books():
    witcher = Book(
        title='Witcher',
        author='Sapkovskiy',
        price=300.0,
        ratting=9.2
    )

    b1984 = Book(
        title='1984',
        author='George Orwell',
        price=199,
        ratting=9.5
    )

    persuasion = Book(
        title='Persuasion',
        author='Jane Austen',
        price=150.0,
        ratting=7.2
    )

    sunset = Book(
        title='Sunset',
        author='Jessie Cave',
        price=425.0,
        ratting=8.1
    )

    db.session.add(witcher)
    db.session.add(b1984)
    db.session.add(persuasion)
    db.session.add(sunset)
    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    print("Populating db ...")
    populate_books()
    print("Successfully populated!")
