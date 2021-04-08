from models import (Base, session, Book, engine)
import csv
import datetime


def menu():
    while True:
        print('''
        \nPROGRAMMING BOOKS
        \r1) ADD BOOK
        \r2) VIEW ALL BOOKS
        \r3) SEARCH FOR BOOK
        \r4) BOOK ANALYSIS
        \r5) EXIT''')
        choice = input('What would you like to do?   ')
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            input('''
            \rPlease choose one of the available options.
            \rA Number from 1-5.
            \rPress enter to try again.''')


# add books to db
# edit books in db
# delete books from db
# search books in db
# data cleaning functions


def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1][:-1])
    year = int(split_date[2])
    return datetime.date(year,month,day)


def clean_price(price_str):
    price_float = float(price_str)
    return int(price_float * 100)


def add_csv():
    with open('suggested_books.csv') as csv_file:
        data = csv.reader(csv_file)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title==row[0]).one_or_none()
            if book_in_db == None:
                title = row[0]
                author = row[1]
                date = clean_date(row[2])
                price = clean_price(row[3])
                new_book = Book(title=title, author=author, published_date=date, price=price)
                session.add(new_book)
        session.commit()


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            # add book
            pass
        elif choice == '2':
            # view books
            pass
        elif choice == '3':
            # search books
            pass
        elif choice == '4':
            # analysis
            pass
        else:
            print('GOODBYE')
            app_running = False



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # app()
    add_csv()

    for book in session.query(Book):
        print(book)