# class Book:
#     ...
# book = Book()
# book.name = input("Name: ")
# book.title =   input("Title: ")
# print("Book Name: ", book.name)
# print("Book Title: ", book.title)

class Book:
    def __init__(self, name: str, title: str, num: int) -> None:
        self.name = name
        self.title = title
        self.num = num
    
    #Getter
    @property
    def num(self):
        return self._num
    
    #Setter
    @num.setter
    def num(self, num):
        self._num = num

    #Getter
    @property
    def name(self):
        return self._name
    
    #Setter
    @name.setter
    def name(self, name):
        self._name = name

    #Getter
    @property
    def title(self):
        return self._title
    
    #Setter
    @title.setter
    def title(self, title):
        if title not in ['Not Applicable', 'Ornamental']:
            raise ValueError("Missing title")
        self._title = title
    
    def __str__(self):
        return f"Book(name={self.name}, title={self.title})"
    
    def __repr__(self):
        return "A book object repr"
    
    def multiply(self, val):
        return self.num * val

name: str = input("Name: ")
title: str = input("Title: ")
try:
    book: Book = Book(name, title, 122)

    print(book)
    print(book.multiply(5))
except ValueError as e:
    print(e)