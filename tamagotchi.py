import time
import random

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
        self.show_inventory()
        
        user_input = input("\nPick the number of the food item you would like to select:")
        item_index = int(user_input) -1
        
        selected_item = self.inventory[item_index]
        if selected_item.type == "food":
            self.hunger -= selected_item.effect
            self.inventory.pop(item_index)
            print(f"\n{self.name} has been feed with {selected_item.name}. Their hunger is now {self.hunger}.")
        else:
            print("Go find some more food!")
    
    def water(self):
        self.show_inventory()

        user_input = input("\nPick the number of the liquid you would like:")
        item_index = int(user_input) -1

        selected_item = self.inventory[item_index]
        if selected_item.type == "liquid":
            self.thirst -= selected_item.effect
            self.inventory.pop(item_index)
            print(f"\n{self.name} has been given {selected_item.name}. Their thirst is now {self.thirst}.")
        else:
            print("The item you are choosing isn't a liquid!")

    def play(self):
        self.show_inventory()

        user_input = input("\nPick the number of toy you would like:")
        item_index = int(user_input) -1 

        item_picked = self.inventory[item_index]
        if item_picked.type == "toy":
            self.thirst -= item_picked.effect
            self.inventory.pop(item_index)
            print(f"\n{self.name}'s happiness has increased by {self.happiness} after playing with {item_picked.name}")


    def use_item(self, item):
        if item.type == "food":
            self.hunger -= item.effect_value
        elif item.type == "toy":
            self.happiness += item.effect_value        
        elif item.type == "liquid":
            self.thirst -= item.effect_value
        else:
            print("You cannot use this item.")

    def money(self):
        print(f"You currently have ${self.inventory} in spending cash.")
    
    def job(self):
        print("\nWhich job would you like to perform?")
        print("1. Picking up trash - 2 dollars per piece of trash")
        print("2. Look for change under vending machines - 1 to 5 dollars based on the vending machine")
        
        user_input = input("\nEnter the number of the job you would like to perform: ")

        if user_input == "1":
            print("Picking up trash...")
            time.sleep(10)
            self.money += 2
        if user_input == "2":
            print("Looking for change...")

    #def shop(self):

    
    #def breed(self):

    #def trade(self):

class breed:
    def __init__(self, breed, traits):
        self.breed = breed
        self.traits = traits

user_name = input("Enter the name of your pet: ")
pet = tamagotchi(user_name) 

pet.inventory.append(item("Pancake", "food", 4))
pet.inventory.append(item("Waffle", "food", 5))
pet.inventory.append(item("Toy Hammer", "toy", 5))
pet.inventory.append(item("Water", "liquid", 3))

while True:

    print("\nWhat would you like to do?")
    print("Options:")
    print("1. Feed")
    print("2. Water")
    print("3. Play")
    print("4. See your savings")
    print("5. Work a job")
    print("6. Exit")

    user_input = input("\nEnter the number of the thing you would like to do: ")

    if user_input == "1":
        pet.feed(pet.inventory[0])
    if user_input == "2":
        pet.water()
    if user_input == "3":
        pet.play()
    if user_input == "4":
        pet.money()
    #if user_input == "5":

    if user_input == "6":
        print("Bye, bye! {pet.name} will be lonely without you.")
        break 

#pet.status()
#pet.feed(pet.inventory[0])
#pet.water()
#pet.play()
#pet.status()



# stored_items = [
#     pancake = item("Pancake", "food", 4),
#     waffle = item("Waffle", "food", 5), 
#     toy_hammer = item("Toy Hammer", "toy", 5),
#     water = item("Water", "liquid", 3), 
#     ]

#pet1 = tamagotchi("dragon", 20, 20, 20, 20)


