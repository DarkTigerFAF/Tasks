from WrittenBook import WrittenBook


class PrintedBook:
    def __init__(self, title, author, ISBN, genre, numOfPages, hardcover):
        super().__init__(title, author, genre, ISBN, numOfPages)
        self.hardcover = hardcover

    def getCoverType(self):
        if self.hardcover == True:
            return "hardcover"
        else:
            return "paperback"

    def printBookInfo(self):
        print(f"*****PrintedBook*****")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.ISBN} - Reference Code: {self.generateReference()}")
        print(f"Genre: {self.genre}")
        print(f"# of Pages: {self.numOfPages}")
        print(f"CoverType: {self.getCoverType()}")
