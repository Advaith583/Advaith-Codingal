class Nike:
    def __init__(self, name):
        self.name = name

    def brand(self):
        print(f"{self.name} has Nike as the brand")

shoe =  Nike("Jordan")
shoe.brand()

class Animal:
  def __init__(self, breed):
    self.breed = breed
 
  def eat(self):
     print(f"{self.breed} is eating ")

  def walk(self):
     print(f"{self.breed} is walking")



dog = Animal("German Shephard")
dog.eat()
dog.walk()
        