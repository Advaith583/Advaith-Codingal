class Nike:
    def __init__(self, ProductName, category):
        self.ProductName = ProductName
        self.category = category

    def details(self):
        print(f'Name of the Product is {self.ProductName} and it belongs {self.category} category')

nikeShoe1 = Nike("Jordan","Shoe")
nikeShoe1.details()
nikeTshirt = Nike("Sports-tshirt","T-shirts")
nikeTshirt.details()

class NikeShoes(Nike):
    def __init__(self, color , model):
        self.color = color
        self.model = model

    def details(self):
        print(f"This is a Nike {self.model} Shoe of {self.color} color.")


Jordan = NikeShoes("Blue", "one")
Jordan.details()
