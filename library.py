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
    
    def availablityTrue(self):
        self.availability = True

    def availablityFalse(self):
        self.availability = False

    def __repr__(self):
        return f'Book ID: {self.__id}, Name: {self.__name}, Author: {self.__author}, Availability: {self.availability}'

item = Library()
book1 = Book(101, "Python Programming", "Jhankar Mahbub", True)
book2 = Book(102, "Habulder Jonno Programming", "Jhankar Mahbub", True)
book3 = Book(103, "Learn JavaScript", "Elliot Smith", True)
book4 = Book(104, "Web Development Basics", "Angela Yu", True)
book5 = Book(105, "Data Structures in C++", "Bjarne Stroustrup", True)
book6 = Book(106, "Machine Learning Guide", "Andrew Ng", True)
book7 = Book(107, "HTML & CSS Design", "Jon Duckett", True)
item.entry_book(book1)
item.entry_book(book2)
item.entry_book(book3)
item.entry_book(book4)
item.entry_book(book5)
item.entry_book(book6)
item.entry_book(book7)


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
        print('\n')
        print("1. View Books")
        print("2. Borrow Books")
        print("3. Return Books")
        print("4. Exit")
        print("Enter Your Choice :")
    elif n == 2:
        print("Enter Your Book ID :")
        x = int(input())
        matched_book = None
        for book in item.book_list:
            if x == book.getID():
                matched_book = book
                break
        if matched_book and matched_book.available():
            matched_book.availablityFalse()
            print("Here is your book, Thank You!")
        else:
            print("This book is not available!")
            
        print('\n')
        print("1. View Books")
        print("2. Borrow Books")
        print("3. Return Books")
        print("4. Exit")
        print("Enter Your Choice :")

    elif n == 3:
        print("Enter Your Book ID :")
        x = int(input())
        matched_book = None
        for book in item.book_list:
            if x == book.getID():
                matched_book = book
                break
        if matched_book:
            matched_book.availablityTrue()
            print("Thank You! Please come again.")
        else:
            print("This is not our book. Thank You!")
            
        print('\n')
        print("1. View Books")
        print("2. Borrow Books")
        print("3. Return Books")
        print("4. Exit")
        print("Enter Your Choice :")

    else :
        break




print('\n\n')