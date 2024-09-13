from Book import Book

class WrittenBook:
    def __init__(self, title, author, genre, ISBN, nPages):
        super().__init__(ISBN, author, title, genre)
        self.numOfPages = nPages
