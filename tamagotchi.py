import time
import random
import threading

class item:
    def __init__(self, name, type, effect):
        self.name = name
        self.type = type
        self.effect = effect
        
class breed:
    def __init__(self, name, traits, income_bonus=1, hunger_decay=1, happiness_increase=1):
        self.name = name
        self.traits = traits
        self.income_bonus = income_bonus
        self.hunger_decay = hunger_decay
        self.happiness_increase = happiness_increase
    
class tamagotchi:
    
    def __init__(self, name):
        self.name = name
        
        self.hunger = 5
        self.energy = 5 
        self.happiness = 5 
        self.thirst = 5
        self.strength = 5
        self.money = 15
        self.inventory = []
        self.alive = True

    #def decay_overtime(self):
        #while self.alive:
            #time.sleep()

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
    
        print(f"{self.name}'s stats: hunger: {self.hunger}, energy: {self.energy}, happiness: {self.happiness}, thirst: {self.thirst}")

    def mood(self):
        if self.hunger <= 3:
            return f"{pet.name} is starving."
        if self.thirst <= 3:
            return f"{pet.name} is dehydrated."
        if self.hunger == 0 or self.thirst == 0:
            self.die() 
            print(f"{pet.name} has died.")
        if self.happiness >= 10:
            return f"{pet.name} is happy."
        if self.happiness >= 6:
            return f"{pet.name} is neutral." 
        if self.happiness >= 3:
            return f"{pet.name} is sad."
           
    def feed(self):
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


    def die(self):
        print(f"{pet.name} has died because you failed to take care of it properly.")
        pet.alive = False


    def play(self):
        self.show_inventory()

        user_input = input("\nPick the number of toy you would like:")
        item_index = int(user_input) -1 

        item_picked = self.inventory[item_index]
        if item_picked.type == "toy":
            self.thirst -= item_picked.effect
            self.inventory.pop(item_index)
            print(f"\n{self.name}'s happiness has increased by {self.happiness} after playing with {item_picked.name}")

    #def use_item(self, item):
        #if item.type == "food":
            #self.hunger -= item.effect_value
        #elif item.type == "toy":
            #self.happiness += item.effect_value        
        #elif item.type == "liquid":
            #self.thirst -= item.effect_value
        #else:
            #print("You cannot use this item.")
            
    def gotcha(self):
        print("Current inventory:")
        self.show_inventory
        
        user_input = input("\nEnter the number of the item you wish to select: ")
        user_index = int(user_input) -1
        
        item_picked = self.inventory[user_index]
        if item_picked.type == "egg":
            print("Hatching your egg...")
            time.sleep(3)
        
        breeds = {
            "Common": [breed("dog", ["loyal"], income_bonus=1)],
            "Rare": [breed("wolf", ["wise"], income_bonus=1.5)],
            "Legendary": [breed("hydra", ["acceptional strength"], income_bonus=2)]
        }
        
    #def trainer(self):

    #def colosseum(self)

    def money(self):
        print(f"You currently have ${self.inventory} in spending cash.")
    
    def job(self):
        print("\nWhich job would you like to perform?")
        print("1. Picking up trash - 2 dollars per piece of trash")
        print("2. Look for change under vending machines - 1 to 5 dollars based on the vending machine")
        
        user_input = input("\nEnter the number of the job you would like to perform: ")

        num = random.randint(1, 5)
        
        if user_input == "1":
            print("Picking up trash...")
            time.sleep(5)
            self.money += 2
            print("You earned 2 dollars!")
        if user_input == "2":
            print("Looking for change...")
            time.sleep(10)
            self.money += num
            print(f"You earned {num} dollars from looking for change!")

    def shop(self, item):
        print("Welcome to the shop!")
         
        stored_items = [
        item("Pancake", "food", 4, 5),
        item("Waffle", "food", 5, 5),
        item("Toy Hammer", "toy", 5, 5),
        item("Water", "liquid", 3, 5),
        item("Apple Juice", "liquid", 3, 5),
        item("Soda", "liquid", 2, 3),
        item("Egg (Common)", "egg", None, 5),
        item("Egg (Rare)", "egg", None, 10),
        item("Egg (Legendary)", "egg", None, 20)
    ]

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

while pet.alive:

    print("\nWhat would you like to do?")
    print("\n=====================================")
    print('Type "help" if you want to know more.')
    print("=====================================")
    print("\nOptions:")
    print("\n1. Feed")
    print("2. Water")
    print("3. Play")
    print("4. Check status")
    print("5. See your savings")
    print("6. Work a job")
    print("7. Exit")

    user_input = input("\nEnter the number of the thing you would like to do: ")

    if user_input == "1":
        pet.feed()
    if user_input == "2":
        pet.water()
    if user_input == "3":
        pet.play()
    if user_input == "4":
        pet.status()
    if user_input == "5":
        pet.money()
    if user_input == "6":
        pet.job()
    if user_input == "7":
        print(f"Bye, bye! {pet.name} will be lonely without you.")
        break 

#pet1 = tamagotchi("dragon", 20, 20, 20, 20)


