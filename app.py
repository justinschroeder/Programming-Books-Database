from models import (Base, session, Book, engine)
# main menu - add, search, analysis, exit, view
# add books to db
# edit books in db
# delete books from db
# search books in db
# data cleaning functions
# loop runs program


if __name__ == '__main__':
    Base.metadata.create_all(engine)