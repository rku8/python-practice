class Book:
    def __init__(self, name: str, author: str, publication_year: int):
        self.name = name
        self.author = author
        self.year = publication_year
    
    def change_year(self, year: int):
        self.year = year

book1 = Book(name="Dynamical system with chaos", author="Ravi", publication_year=2023)
print(book1.name)
print(book1.name)