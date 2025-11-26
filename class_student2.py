class car: 
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def show_info(self):
        print(f"the car brand is {self.brand} and the color is {self.color}")

car1 = car("Lamorgini", "green")
car1.show_info()

car2 = car("Maruti Suzuki", "White")
car2.show_info()
