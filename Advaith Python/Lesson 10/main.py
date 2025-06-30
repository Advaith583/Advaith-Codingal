class Car:
    def __init__(self,model,engine):
        self.model = model
        self.engine = engine
        print(f"the {self.model}'s object has been created")

    def start(self):
        print("Vroom Vroom !!")

    def stop(self):
        print("car is stopped!!")

    def details(self):
        print(f"the {self.model} car has a {self.engine} engine.")

    def __del__(self):
        print(f"{self.model}'s object has been deleted")

bmwOBJ = Car("BMW m5", "petrol")
bmwOBJ.start()
bmwOBJ.stop()
bmwOBJ.details()

del bmwOBJ
