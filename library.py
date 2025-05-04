class Library:
    def __init__(self):
        self.book_list = []

    def entry_book(self, book):
        self.book_list.append(book)


class Book:
    def __init__(self, id, name, author, availability):
        self.__id = id
        self.__name = name
        self.__author = author
        self.availability = availability

    def getID(self):
        return self.__id

    def available(self):
        return self.availability

    def borrow_book(self):
        if self.availability:
            self.availability = False
            print("Here is your book, Thank You!")
        else:
            print("This book is not available!")

    def return_book(self):
        self.availability = True
        print("Thank You! Please come again.")

    def __repr__(self):
        return f'Book ID: {self.__id}, Name: {self.__name}, Author: {self.__author}, Availability: {"Yes" if self.availability else "No"}'


item = Library()
item.entry_book(Book(101, "Python Programming", "Jhankar Mahbub", True))
item.entry_book(Book(102, "Habulder Jonno Programming", "Jhankar Mahbub", True))
item.entry_book(Book(103, "Learn JavaScript", "Elliot Smith", True))
item.entry_book(Book(104, "Web Development Basics", "Angela Yu", True))
item.entry_book(Book(105, "Data Structures in C++", "Bjarne Stroustrup", True))
item.entry_book(Book(106, "Machine Learning Guide", "Andrew Ng", True))
item.entry_book(Book(107, "HTML & CSS Design", "Jon Duckett", True))


def viewBooks():
    for book in item.book_list:
        print(book)


print('\n\n')
print("1. View Books")
print("2. Borrow Books")
print("3. Return Books")
print("4. Exit")
print("Enter Your Choice :")

while True:
    n = int(input())
    if n == 1:
        print('\n')
        viewBooks()

    elif n == 2:
        print("Enter Your Book ID :")
        x = int(input())
        matched_book = None
        for book in item.book_list:
            if book.getID() == x:
                matched_book = book
                break

        if matched_book:
            matched_book.borrow_book()
        else:
            print("Book not found!")

    elif n == 3:
        print("Enter Your Book ID :")
        x = int(input())
        matched_book = None
        for book in item.book_list:
            if book.getID() == x:
                matched_book = book
                break

        if matched_book:
            matched_book.return_book()
        else:
            print("This is not our book. Thank You!")

    elif n == 4:
        break
    else:
        print("Invalid choice!")

    print('\n')
    print("1. View Books")
    print("2. Borrow Books")
    print("3. Return Books")
    print("4. Exit")
    print("Enter Your Choice :")

# finished the work!
