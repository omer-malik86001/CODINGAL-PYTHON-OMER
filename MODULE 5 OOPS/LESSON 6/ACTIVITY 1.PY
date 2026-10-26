from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        print("animal can  move and communicate")

class Dog(animal):
    def move(self):
        print("the dog can walk and run")

class human(animal):
    def move(self):
        print("the human can walk and run")

class cat(animal):
    def communicate(self):
        print("the cat can jump")
    def move(self):
        print("the cat can walk and run")

a=Dog()
a.move()
h=human()
h.move()
s=cat()
s.move()
s.communicate()









