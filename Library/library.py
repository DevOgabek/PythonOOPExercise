class Library:
    def __init__(self) -> None:
        self.library_data =  [[[[[] for _ in range(10)] for _ in range(6)] for _ in range(30)] for _ in range(3)]

    def add(self, book, floor, shelf, closet, position):
        self.library_data[floor - 1][shelf - 1][closet-1].insert(position - 1, book)

    def contains(self, book):
        for floor in range(3):
            for shelf in range(30):
                for closet in range(6):
                    if book in self.library_data[floor][shelf][closet]:
                        position = self.library_data[floor][shelf][closet].index(book) + 1
                        return f"{book} book {floor + 1}-floor, {shelf + 1}-shelf, {closet +1}-closet, {position}-is located in the position."
        return f"{book} book not found in library."
    
    def get_books(self, floor, shelf, closet):
        for book in self.library_data[floor][shelf][closet]:
            if book:
                print(f"{book.author}, {book.name}")

    def get_floor(self, book):
        for floor in range(3):
            for shelf in range(30):
                for closet in range(6):
                    if book in self.library_data[floor][shelf][closet]:
                        return f"{book} book at {floor+1}-floor."
        return f"{book} book not found at floor."

    def get_shelf(self, book):
        for floor in range(3):
            for shelf in range(30):
                for closet in range(6):
                    if book in self.library_data[floor][shelf][closet]:
                        return f"{book} book at {floor+1}-shelf."
        return f"{book} book not found at shelf." 

    def get_closet(self, book):
        for floor in range(3):
            for shelf in range(30):
                for closet in range(6):
                    if book in self.library_data[floor][shelf][closet]:
                        return f"{book} book at {closet+1}-closet."
        return f"{book} book not found at closet." 
    
    def find(self, name, author):
        for floor in range(3):
            for shelf in range(30):
                for closet in range(6):
                    for position in range(10):
                        if self.library_data[floor][shelf][closet][position]:
                            if self.library_data[floor][shelf][closet][position].name == name and self.library_data[floor][shelf][closet][position].author == author:
                                return f"{name} book of {author} at {floor + 1}-floor, {shelf + 1}-shelf, {closet +1}-closet, {position}-is located in the position."
        return f"{name} book not found in library." 