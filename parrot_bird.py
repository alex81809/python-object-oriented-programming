class Parrot: 
    def __init__(self, name, color):
        self.name = name
        self.color = color 
    
    def sing(self):
        print(f"{self.name} is singing!")
    
    def dance(self):
        print(f"{self.name} is dancing!")

Parrot1 = Parrot("Buddy", "green")
Parrot1.sing()
Parrot1.dance()

Parrot2 = Parrot("Clichy", "blue")
Parrot2.sing()
Parrot2.dance()
