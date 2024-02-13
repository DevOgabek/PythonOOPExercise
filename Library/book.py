class Book:
    def __init__(self, name, author) -> None:
        self.name = name
        self.author = author
    
    def get_name(self):
        return self.name
    
    def get_author(self):
        return self.author   
    
    def __str__(self):
        return f"{self.name}, {self.author}"