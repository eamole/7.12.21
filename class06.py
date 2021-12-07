# animals - 02
class Animal:

    # class property/variable
    animals = [] # list of every animal
    
    def __init__(self, breed, name, color, legs = 4):
        # instance variables
        self.breed = breed
        self.legs = legs
        self.color = color
        self.name = name
        Animal.animals.append(self) # store myself in the shared list

    def __str__(self):
        template = "Breed : {:>8} \nName : {:>8}\nColor : {:>8}\nLegs : {:>8}"
        out = template.format(self.breed, self.name, self.color, self.legs)
        return out

    @classmethod    # decorator
    def print(cls):
        for animal in cls.animals:
            print(animal)
            print()

class Dog(Animal):
    def __init__(self, name, color, legs = 4):
        # should be done this way - call the original constructor
        super().__init__("Dog", name, color, legs)

class Giraffe(Animal):
    def __init__(self, name, color, legs = 4):
        super().__init__("Giraffe", name, color, legs)
        
Dog("Fido", "Brown")
Giraffe("LongNeck", "Yellow")


# can we create a class function/method like a class property?
##print(Animal.animals)
Animal.print()

##print(dog)

##Dog.print()




