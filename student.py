class Student:
    def __init__(self, name: str, age: int, pincode: int , grade: int) -> None:
        self.name = name
        self.age = age
        self.pincode = pincode
        self.grade = grade

    def show_names(self) -> str:
        return self.name
    
    def show_age(self) -> int:
        return self.age
    
    def change_pincode(self, other: int):
        self.pincode = other
    
    def show_pincode(self) -> int:
        return self.pincode
    
    def show_grade(self) -> int:
        return self.grade
    

ravi = Student(name='Ravi', age=24, pincode=226401, grade=12)

print("Name:", ravi.name)
print("Age:", ravi.age)
print("Class:", ravi.grade)
        
ravi.change_pincode(227101)

print("Name:", ravi.name)
print("Age:", ravi.age)
print("Pincode:", ravi.pincode)