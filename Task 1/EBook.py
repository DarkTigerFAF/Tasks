from WrittenBook import WrittenBook

class EBook:
    def __init__(self, title, author, ISBN, genre, numOfPages, size):
        super().__init__(title, author, genre, ISBN, numOfPages)
        self.size = size

    def getSize(self):
        return self.size

    def printBookInfo(self):
        print(f"*****EBook*****")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.ISBN} - Reference Code: {self.generateReference()}")
        print(f"Genre: {self.genre}")
        print(f"# of Pages: {self.numOfPages}")
        print(f"Book Size: {self.size}")