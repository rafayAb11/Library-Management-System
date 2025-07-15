class Library:
    def __init__(self):
        self.books = []
        
    def addBook(self,book):
        self.books.append(book)
        print(f"{book} has been added into the library")

    def showInfo(self):
        print(f"Total Books: {len(self.books)}\n")

    def showAllBooks(self):
        if not self.books:
            print("No books available")
        else:
            print("\nList of Books:")
            for i, book in enumerate(self.books,1):
                print(f"{i}.{book}")

def main():
    library = Library()
    while True:
        print("\nLibrary menu")
        print("\n1. Add Book\n2. Show total books\n3. Show all books\n4. Exit")

        choice = input("\nEnter your action: ")

        if choice == "1":
            title = input("Enter book title: ")
            library.addBook(title)

        elif choice == "2":
            library.showInfo()

        elif choice == "3":
            library.showAllBooks()

        elif choice == "4":
            print("Exiting the program....")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()