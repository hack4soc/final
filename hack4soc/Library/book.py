
class book:

    def __init__(self):

        self.name = ""
        self.genre = ""
        self.level = 0 #A-1. B-2, C-3, D-4, E-5
        self.publisher = ""

    def setLevel(self):
        n = int(input("Enter the level of the book : "))
        if n in range(1, 6):
            self.level = n
    
    def setName(self):
        st = input("Enter the name of the book : ")
        if st:
            self.name = st
        
    def setGenre(self):
        st = input("Enter the genre : ")
        if st:
            self.genre = st

    def setPublisher(self):
        st = input("Enter the publisher :")
        if st:
            self.publisher = st




    