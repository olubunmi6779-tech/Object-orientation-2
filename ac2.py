class libary:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following books in our libary: {self.name}")
        for book in self.bookLis:
            print(book)
    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book has been updated, You can borrow the book now")
        else:
            print(f"Book is already being/used by {self.lendDict[book]}")
        
        def addBook(self, book):
            self.bookList.append(book)
            print("Book has been added to book list")

            
        
        def returnBook(self, book):
            self.lendDict.pop(book)
if __name__ == '__main__':

    books = libary (['Python', 'Harry potter', 'Forever young', 'Love like no other', 'A beutiful dream'],"Let's upSkill" ) 

while(True):
    print(f"Welcome to the {books.name} libary , kindly enter your choice to continue")

    print("1. Display Books")
    print("2. Lend a book")
    print("3. Add a book")
    print("4. Return a book") 
    user_choice = input
    if user_choice not in ['1', '2', '3', '4',]:
        print("Please enter a valid option")
        continue

    else:
        user_choice = int(user_choice)

    if user_choice == 1:
        books.displayBooks()
    elif user_choice == 2:
        book = input("Enter the name of the book you want to lend: ")
        user = input("Enter your name")
        books.lendBook(user, book)
    elif user_choice == 3:
        book = input("Enter the name of the book you want to add:")
        books.addBook(book)
    elif user_choice == 4:
        book = input("Enter the name of the book you want to return")
        books.returnBook(book)
    
    else:
        print("Not a VALID OPTION")

    print("PRESS Q to quit & C to continue")
    user_choice2 = ""
    while(user_choice2!="C" and user_choice2!="Q"):
        user_choice2 = input()
        if user_choice2 == "Q":
           exit()
        elif user_choice2 =="C":
            continue

