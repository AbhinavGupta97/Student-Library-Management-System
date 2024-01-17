class Library:
    def __init__(self, listofbooks):
        self.books = listofbooks
    
    def displayBooks(self):
        self.books.sort()
        for book in self.books:
            print("\t ->", book)

    def borrowBook(self, bookname):
        if bookname in self.books:
            print(f"You have been issued book name '{bookname}'")
            print("Please return it in 30 days, if not 1 rs, per day fine will be imposed.")
            self.books.remove(bookname)
        else:
            ("Sorry this book is not available.")

    def addBook(self, bookname):
        self.books.append(bookname)
        print(f"Return of book '{bookname}' is successful")

class Student:
    def req_book(self):
        print("enter 'q' to quit")
        self.book = input("Please enter the name of the book you want to borrow :")
        if self.book =='q':
            print("")
        else:
            return self.book

    def return_book(self):
        print("enter 'q' to quit")
        self.book = input("Enter the name of the book you want to return :")
        if self.book =='q':
            print("")
        else:
            return self.book
    
    def donate_book(self):
        print("enter 'q' to quit")
        self.book = input("Enter the name of the book you want to donate :")
        if self.book =='q':
            print("")
        else:
            return self.book

if __name__=="__main__":

    central_Library = Library(["Darvin", "Inception", "Science", "Marvels", "Democracy", "Costitution", "Geography", "History"])
    
    Welcome_Msg = '''    *************************
    Welcome to 'Digital Lirary'.
    *************************'''

    option_menu = '''Please choose from below options.
    1> Display the available books.
    2> Request book.
    3> Return book.
    4> Donate book.
    5> Exit.'''

    student = Student()

    print(Welcome_Msg)

    while(True):

        print(option_menu)

        Student_choise = input("Enter your choise :")

        if Student_choise == '1':
            central_Library.displayBooks()
        
        elif Student_choise == '2':
            central_Library.borrowBook(student.req_book())
        
        elif Student_choise == '3':
            central_Library.addBook(student.return_book())

        elif Student_choise == '4':
            central_Library.addBook(student.donate_book())
       
        elif Student_choise == '5':
            print("Thank you for using 'Digital Library'")
            print("-----------------------------------------------------------")
            print(Welcome_Msg)
            #exit()

        elif Student_choise =='quit':
            exit()
        else:
            print("Please enter valid choise!")
            print("\n")