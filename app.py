from sqlalchemy.sql.coercions import expect_col_expression_collection
from models import (Base, session, Book, engine)
import csv
import datetime
import time


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
    try:
        month = int(months.index(split_date[0]) + 1)
        day = int(split_date[1][:-1])
        year = int(split_date[2])
        date = datetime.date(year,month,day)
    except ValueError:
        print('''
        \n**********DATE ERROR**********
        \rEnter Date as Month Day, Year.
        \rEx: January 1, 2021
        \rPress enter to try again.
        \r******************************''')
        return
    else:
        return date


def clean_price(price_str):
    try:
        price_float = float(price_str)
    except ValueError:
        print('''
        \n**********PRICE ERROR**********
        \rEnter price as number without currency symbol.
        \rEx: 10.99
        \rPress enter to try again.
        \r*******************************''')
        return
    else:
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
            title = input('Title: ')
            author = input('Author: ')
            date_error = True
            while date_error:
                date = input('Published Date (Ex: January 1, 2021): ')
                date = clean_date(date)
                if type(date) == datetime.date:
                    date_error = False
            price_error = True
            while price_error:
                price = input('Price (Ex: 10.99): ')
                price = clean_price(price)
                if type(price) == int:
                    price_error = False
            new_book = Book(title=title, author=author, published_date=date, price=price)
            session.add(new_book)
            session.commit()
            print('Book Added!')
            time.sleep(1.5)
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
    add_csv()
    app()
    
    for book in session.query(Book):
        print(book)