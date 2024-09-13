class Book:
    def __init__(self):
        self.ISBN = None
        self.author = None
        self.title = None
        self.genre = None

    def __init__(self, ISBN, author, title, genre):
        self.ISBN = ISBN
        self.author = author
        self.title = title
        self.genre = genre

    def setISBN(self, ISBN):
        self.ISBN = ISBN

    def setAuthor(self, author):
        self.author = author

    def setTitle(self, title):
        self.title = title

    def setGenre(self, genre):
        self.genre = genre

    def getISBN(self):
        return self.ISBN

    def getAuthor(self):
        return self.author

    def getTitle(self):
        return self.title

    def getGenre(self):
        return self.genre

    def generateReference(self):
        return (self.author[0:2]).upper() + '-' + (self.genre[0:2]).upper()

    def verifyISBN(self, ISBN):
        sum = 0
        for i in range(0, 3):
            sum += int(ISBN[i]) * (3 - i)
        return (sum % 4) == (int(ISBN[3]))
