# sample classes
class Animal:
    def __init__(self, breed, name, color, legs = 4):
        self.breed = breed
        self.legs = legs
        self.color = color
        self.name = name

    def __str__(self):
        template = "Breed : {:>8} \nName : {:>8}\nColor : {:>8}\nLegs : {:>8}"
        out = template.format(self.breed, self.name, self.color, self.legs)
        return out

    def speak(self):
        print("Hello! from ", self.name)

class Dog(Animal):
    def speak(self):
        print("Woof woof! from ", self.name)
    
class Cat(Animal):
    def speak(self):
        print("Meow! from ", self.name)

class Cow(Animal):
    def speak(self):
        print("Mooo! from ", self.name)

class Person(Animal):
    pass

class WildCat(Cat):
    def speak(self):
        print("ROAR! from ", self.name)



animals = []
rover = Dog("Dog", "Rover", "Brown")
animals.append(rover)
animals.append(Cat("Cat", "Felix", "Black"))
animals.append(Cow("Cow", "Daisy", "Brown"))
animals.append(WildCat("WildCat", "Leo", "Yellow"))
animals.append(Person("Human", "Mary", "White", 2))

for animal in animals:
    print(animal)
    animal.speak()
    print()
