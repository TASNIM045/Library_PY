class Library:
    book_list = []
    
    def entry_book(self):
        print("ok")

class Book(Library):
    def __init__(self,book_id,book_title,book_author,book_availablity):
        self.__book_id = book_id
        self.__book_title = book_title
        self.__book_author = book_author
        self.book_availablity = book_availablity

        # self.entry_book()

    def getID(self):
        return self.__book_id

    



obj1 = Book(101,'Python Programing','Jhankar Mahbub',True)
obj2 = Book(102,'C++','Abdul Kalam',True)
obj3 = Book(103,'DSA','Makbul Hossain',True)
obj4 = Book(104,'Physich','Misha Chowdhory',True)
obj5 = Book(105,'Chemistry','Sakib Khan',True)
obj6 = Book(106,'Dry Cake','Azad Bhaiya',True)
obj7 = Book(107,'Ghi Toast','Kamal Khan',True)
obj8 = Book(107,'Easy','Poster Man',True)
books = Library()

for i in range(1,9):
    books.book_list.append(f'obj{i}')


print("\n\n")
print("------------Welcome To Our Library------------")
print("1. Book List")
print("2. Borrow Books")
print("3. Return Books")
print("4. Exits")

print("Please Enter Your choice : ") 


while True:
    n = int(input())
    if n is 1:
        print(1)
    elif n is 2:
        print(2)
    elif n is 3:
        print(3)
    else:
        break

print("\n\n")

