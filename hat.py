import random

class Hat:
    houses = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Hermione']

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Ravi")