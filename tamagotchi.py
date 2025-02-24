class item:
    def __init__(self, name, effect, type):
        self.name = name
        self.type = type
        self.effect = effect

class tamagotchi:
    
    def __init__(self, name):
        self.name = name
        
        self.hunger = 5
        self.energy = 5 
        self.happiness = 5 
        self.thirst = 5
        self.money = 15
        self.inventory = []

    def inventory(self):
        if not self.inventory:
            return "Your inventory is empty."
        
        print(self.inventory)
        print("\nInventory: ")
        for index, item in enumerate(self.inventory):   
            
            
    
    def status(self):
        item_names = []
        
        for item in self.inventory:
            item_names.append(item.name)
            
        print(f"Inventory: {item_names}")
        print(f"{self.name}'s stats: hunger: {self.hunger}, energy: {self.energy}, happiness: {self.happiness}, thirst: {self.thirst}")
    
    def feed(self):
        if not self.inventory:
            return "You have no food to feed your pet with."
        
                

pancake = item("Pancake", "food", 4)
waffle = item("Waffle", "food", 5)    
toy_hammer = item("Toy Hammer", "toy", 6)

pet1 = tamagotchi("dragon", 20, 20, 20, 20)

user_name = input("Enter the name of your pet: ")

pet = tamagotchi(user_name) 

pet.status()


#def play():

        
#def water():