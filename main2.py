class library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
    
    def displayAvaliableBooks(self) :
        print ("The current present books are:")
        for books in self.books:
            print ("\t *" +books)

    def borrowBook (self, bookName):
        if bookName in self.books:
            print (f"You have been issued {bookName}. please keep it safe and return it in 30 days.")
            self.books.remove(bookName)
            return True

        else:
            print ("Sorry the book has been issued to someone else or it is not avaliable in our library now.... ")
            return False

    def returnbook (self, bookName):
        self.books.append(bookName)
        print ("Thanks for using our library and hope you enjoyed the book!!")


class students:
    def __init__(self, listOfStudents):
        self.students = listOfStudents

    def displayAvaliableStudents (self) :
        print ("The current present students are:")
        for student in self.students:
            print ("\t *" +student)

    def newStudent(self, name):
        self.students. append(name)
        print(f"The new student {name} is added.")

    def removestudent(self, name):
        if name in self.students:
            print(f"The student {name} was removed.")
            self.students .remove (name)
            return True

        else:
            print (f"There Is No Student Named {name}....")
            return False
        

    def requestBook(self):
        self.book = input("Enter the book name you want to borrow / delete:\n")
        return self.book

    def returnBook(self):
        self.book = input("Enter the book name you want to add / return:\n")
        return self.book

class extra:

    def __init__(self, listOfStudents):
        self.students = listOfStudents

    def addNewStudent (self):
        self.students = input("Enter The Student's Name:\n")
        return self.students

    def removeStudent (self):
        self.students = input ("Enter The Student You Want To Remove:\n")
        return self.students


if __name__ == "__main__":
    X = library(["A Tale of Two Cities", "The Little Prince", "Harry Potter and the Philosopher's Stone", "And Then There Were None", "Dream of the Red Chamber", "The Hobbit"])
    Y = students(["Aniket"])
    Z = extra([""])
    #MyLibrary.displayAvaliableBooks()

    while (True):
        welcomemsg = '''
        ====== WELCOME TO MYLIBRARY =====
        please choose an option press the number to select an option
       1. Student's Option 
       2. Librarian's Option 
       3. Exit the library.
        '''
        print(welcomemsg)
        a = int(input ("enter a choice:\n"))
        if a == 1:
            while (True):
                StudentsOption = '''
                ====== WELCOME TO STUDENTS MENU ======
                please choose an option press
                1. Display The Present Books
                2. Request A Book 
                3. Add/Return A Book 
                4. Exit The Library '''
                
                print(StudentsOption)
                b = int (input("Enter Your Choice:\n"))

                if b == 1 :
                    X.displayAvaliableBooks()
                
                elif b == 2 :
                    X.borrowBook(Y.requestBook())

                elif b == 3 :
                    X.returnbook(Y.returnBook())

                elif b == 4 :
                    print ("Thank you for using our library...")
                    exit()
                
                else :
                    print ("Invalid Choice!!!")

        elif a == 2:
            while (True):
                LibrarianMenu = '''
                ====== WELCOME TO LIBRARIAN'S MENU ======
                1. Display The Present Books.
                2. Display The Present Students.
                3. Add New Student.
                4. Remove Old Student.
                5. Add Books.
                6. Delete A Book. 
                7. Exit The Library.'''

                print(LibrarianMenu)
                c = int (input("Enter Your Choice:\n"))

                if c == 1 :
                    X.displayAvaliableBooks()

                elif c == 2 :
                    Y.displayAvaliableStudents()
                
                elif c == 3 :
                    Y.newStudent(Z.addNewStudent())
                
                elif c == 4 :
                    Y.removestudent(Z.removeStudent())

                elif c == 5 :
                    X.returnbook(Y.returnBook())

                elif c == 6 :
                    X.borrowBook(Y.requestBook())

                elif c == 6 :
                    print ("Thank you for using our library...")
                    exit()

                else:
                    print ("Invalid Choice!!!")
        

        elif a == 3:
            print ("Thank you for using our library...")
            exit()

        else:
            print("Invalid choice!!!")

        