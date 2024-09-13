from Book import Book

class AudioBook:
    def __init__(self, title, author, genre, ISBN, duration, narrator):
        super().__init__(ISBN, author, title, genre)
        self.duration = duration
        self.narrator = narrator

    def getDuration(self):
        return self.duration

    def getNarrator(self):
        return self.narrator

    def printBookInfo(self):
        print(f"*****AudioBook*****")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.ISBN} - Reference Code: {self.generateReference()}")
        print(f"Genre: {self.genre}")
        print(f"Duration: {self.duration}")
        print(f"Narrator: {self.narrator}")