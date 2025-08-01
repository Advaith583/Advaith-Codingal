# class Student :
#     def __init__(self,name,course,number):
#         self.name = name
#         self.course = course
#         self.__number = number

#     def details(self):
#         print(f'The name of the student is {self.name},and the course taken by the student is {self.course}.')   

#     def get_number(self):
#         print(f"THe number of the student is :", self.__number)

#     def set_number(self, newNumber):
#         self.__number = newNumber
#         print("The number has been updated", self.__number)

# st1 = Student("Advaith", "WebDev",998899)

# print(st1.name)
# print(st1.course)
# st1.get_number()
# st1.set_number(888888)
# st1.details()

class Animal:
   def make_sound(self):
      return "Some generic animal sound"
   
class Dog(Animal):
   def make_sound(self):
      return "Bark"
   
class Cat(Animal):
   def make_sound(self):
      return "Meow"
   
dog = Dog()
print(dog.make_sound())
cat = Cat()
print(cat.make_sound())