from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Bird(Animal):
    def move(self):
        print("I can fly")
class Lion(Animal):
    def move(self):
        print("I can run fast and roar")

r = Human()
r.move()
s = Snake()
s.move()
b = Bird()
b.move()
l = Lion()
l.move()