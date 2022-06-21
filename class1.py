# class1.py

class Person:
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("my name is {0}".format(self.name))

p1 = Person()
p1.print()