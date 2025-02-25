class item:
    def __init__(self, name, type, effect):
        self.name = name
        self.type = type
        self.effect = effect
        
class tamagotchi:
    
    def __init__(self, name):
        self.name = name
        
        self.hunger = 10
        self.energy = 5 
        self.happiness = 5 
        self.thirst = 5
        self.money = 15
        self.inventory = []

class breed:
    def __init__(self, breed, traits):
        self.breed = breed
        self.traits = traits

    def show_inventory(self):
        if not self.inventory:
            return "Your inventory is empty."
    
        print("\nInventory: ")
        for index, item in enumerate(self.inventory, 1):
            print(f"{index}. {item.name}")   
            

    
    def status(self):
        item_names = []
        
        for item in self.inventory:
            item_names.append(item.name)
            
        #print(f"Inventory: {item_names}")
        print(f"{self.name}'s stats: hunger: {self.hunger}, energy: {self.energy}, happiness: {self.happiness}, thirst: {self.thirst}")
    
    def feed(self, item):
        if not self.inventory:
            return "Inventory is empty."
            
        self.show_inventory()
        
        user_input = input("\nPick the number of the item you would like to select:")
        item_index = int(user_input) -1
        
        selected_item = self.inventory[item_index]
        if selected_item.type == "food":
            self.hunger -= selected_item.effect
            print(f"{self.name}, has been feed with {selected_item}. They're hunger is now {self.hunger}.")
        else:
            print("Go find some more food!")
            

            
    def use_item (self, item):
        if item.type == "food":
            self.hunger -= item.effect_value
        elif item.type == "toy":
            self.happiness += item.effect_value        
        elif item.type == "liquid":
            self.thirst -= item.effect_value
        else:
            print("You cannot use this item.")

        

pancake = item("Pancake", "food", 4)
waffle = item("Waffle", "food", 5)    
toy_hammer = item("Toy Hammer", "toy", 5)
water = item("Water", "liquid", 3)

pet1 = tamagotchi("dragon", 20, 20, 20, 20)

user_name = input("Enter the name of your pet: ")

pet = tamagotchi(user_name) 

#def play():

        
#def water():