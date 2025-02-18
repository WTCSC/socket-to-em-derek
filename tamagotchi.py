class tomogotchi:
    
    def __init__(self, name):
        self.name = name
        
        self.hunger = 5
        self.energy = 5 
        self.happiness = 5 
        self.thirst = 5

        
    def status(self):
        print(f"{self.name}'s stats: hunger: {self.hunger}, energy: {self.energy}, happiness: {self.happiness}, thirst: {self.thirst}")
        
user_name = input("Enter the name of your pet: ")

pet = tomogotchi(user_name)

pet.status()

    def play():

    def feed():
        
    def water():