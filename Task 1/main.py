from Book import Book
from Library import Library


class TestLibrary:
    @staticmethod
    def main():
        library = Library()
        library.MAX_SIZE = 100

        while True:
            print("\nLibrary Menu:")
            print("1) Add a book")
            print("2) Delete a book")
            print("3) Find a book")
            print("4) List all books")
            print("5) List books for a given genre")
            print("6) Number of books for a given author")
            print("7) Total number of books")
            print("8) Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                ISBN = input("Enter ISBN: ")
                author = input("Enter author: ")
                title = input("Enter title: ")
                genre = input("Enter genre: ")
                book = Book(ISBN, author, title, genre)
                if library.addBook(book):
                    print("Book added successfully.")
                else:
                    print("Failed to add book.")

            elif choice == '2':
                ISBN = input("Enter ISBN of the book to delete: ")
                library.deleteBook(ISBN)
                print("Book deleted if it existed.")

            elif choice == '3':
                ISBN = input("Enter ISBN of the book to find: ")
                index = library.findBook(ISBN)
                if index != -1:
                    print("Book found at index:", index)
                else:
                    print("Book not found.")

            elif choice == '4':
                library.printAll()

            elif choice == '5':
                genre = input("Enter genre: ")
                library.printGenre(genre)

            elif choice == '6':
                author = input("Enter author: ")
                count = library.getNumberOfBooksByAuthor(author)
                print(f"Number of books by {author}: {count}")

            elif choice == '7':
                total = library.getNumberOfBooks()
                print(f"Total number of books: {total}")

            elif choice == '8':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    TestLibrary.main()
