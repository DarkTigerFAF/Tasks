from Book import Book


class Library:
    def __init__(self):
        self.libraryBooks = []
        self.numOfBooks = 0
        self.MAX_SIZE = 0

    def addBook(self, *args):
        if isinstance(args[0], Book):
            book = args[0]
        else:
            isbn, author, title, genre = args
            book = Book(isbn, author, title, genre)

        if book.verifyISBN(book.getISBN()) and self.findBook(book.getISBN()) == -1 and self.numOfBooks < self.MAX_SIZE:
            self.libraryBooks.append(book)
            self.numOfBooks += 1
            return True
        else:
            return False

    def deleteBook(self, ISBN):
        for i in range(0, len(self.libraryBooks)):
            if self.libraryBooks[i].getISBN() == ISBN:
                self.libraryBooks[i] = self.libraryBooks[-1]
                self.libraryBooks.pop()

    def findBook(self, book):
        if isinstance(book, Book):
            for i in range(0, len(self.libraryBooks)):
                if self.libraryBooks[i] == book:
                    return i
        else:
            for i in range(0, len(self.libraryBooks)):
                if self.libraryBooks[i].getISBN() == book:
                    return i
        return -1

    def printAll(self):
        for book in self.libraryBooks:
            book.printBookInfo()

    def printGenre(self, genre):
        for book in self.libraryBooks:
            if book.getGenre() == genre:
                book.printBookInfo()

    def getNumberOfBooksByAuthor(self, author):
        cnt = 0
        for book in self.libraryBooks:
            if book.getAuthor() == author:
                cnt += 1
        return cnt

    def getNumberOfBooks(self):
        return self.numOfBooks
