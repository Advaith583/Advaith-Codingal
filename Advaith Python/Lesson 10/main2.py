class Student:
    def __init__(self, name, age, grade):

        self.name = name
        self.age = age
        self.grade = grade
        print(f"\nstudent record created for {self.name}.")


    def showDetails(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Grade:{self.grade}")

    def updateGrade(self, new_grade):
        self.grade = new_grade
        print(f"{self.name}'s grade has been updated to {self.grade}.")

    def  __del__(self):
        print(f"Student record for {self.name} has been deleted.")

student = Student("Anjali" , 14, "8th")
student.showDetails()

del student
