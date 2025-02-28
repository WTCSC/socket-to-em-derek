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
        self.happiness = 5 
        self.thirst = 5
        self.money = 15
        self.inventory = []
        self.alive = True

    def decay_overtime(self):
        while self.alive:
            time.sleep(200)
            self.hunger = min(20, self.hunger + 1)
            self.thirst = min(20, self.thirst + 1)
            self.happiness = max(0, self.happiness - 1)

            if self.hunger >= 20:
                print(f"{pet.name} has straved to death.")
                self.die()
                break
            if self.thirst >= 20:
                print(f"{pet.name} has died of dehydration.")
                self.die()
                break
    
    def auto_decay(self):
        decay_thread = threading.Thread(target=self.decay_overtime)
        decay_thread.daemon = True
        decay_thread.start()        

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
            return
        
    
        print("\nInventory: ")
        for index, item in enumerate(self.inventory, 1):
            print(f"{index}. {item.name}")   
            
    
    def status(self):
        item_names = []
        
        for item in self.inventory:
            item_names.append(item.name)
    
        print(f"{self.name}'s stats:")
        print(f"Hunger: {self.hunger}"), 
        print(f"Energy: {self.energy}"), 
        print(f"Happiness: {self.happiness}") 
        print(f"Thirst: {self.thirst}")
        print(f"Money: {self.money}")

    def mood(self):
        if self.hunger >= 15:
            return f"{self.name} is starving." 
        if self.thirst >= 15:
            return f"{self.name} is dehydrated."
        if self.happiness >= 10:
            return f"{self.name} is happy."
        if self.happiness >= 6:
            return f"{self.name} is neutral." 
        if self.happiness >= 3:
            return f"{self.name} is sad."
        return f"{self.name} is in a very bad mood."
    
    def auto_mood(self):
        mood_thread = threading.Thread(target=self.auto_mood)
        mood_thread.deamon = True
        mood_thread.start()

    def monitor_mood(self):
        while self.alive:
            time.sleep(60)
            print(self.mood())

    def feed(self):
        if not self.alive:
            print(f"{self.name} is dead.")
            return 
        
        while True:

            self.show_inventory()
            
            user_input = input('\nPick the number of the food you would like to select or type "exit" to go back: ')
            
            if user_input.lower() == "exit":
                break

            try:
                
                item_index = int(user_input) - 1

                selected_item = self.inventory[item_index]
                if selected_item.type == "food":
                    self.hunger = max(0, self.hunger - selected_item.effect)
                    self.inventory.pop(item_index)
                    print(f"\n{self.name} has been feed with {selected_item.name}. Their hunger is now at {self.hunger}.")
                else:
                    print("Go find some more food!")

            except ValueError:
                print("Please enter a valid number or exit to go back.")
        
    def water(self):
        if not self.alive:
            print(f"{self.name} is dead.")
            return

        while True:
            self.show_inventory()

            user_input = input('\nPick the number of the liquid you would like to select or type "exit" to go back: ')

            if user_input.lower() == "exit":
                break
            
            try:

                item_index = int(user_input) - 1

                selected_item = self.inventory[item_index]
                if selected_item.type == "liquid":
                    self.thirst = max(0, self.thirst - selected_item.effect)
                    self.inventory.pop(item_index)
                    print(f"\n{self.name} has been given {selected_item.name}. Their thirst is now {self.thirst}.")
                else:
                    print("The item you are choosing isn't a liquid!")
            except ValueError:
                print('Please enter a valid number or type "exit" to return.')

    def die(self):
        
        print(f"{pet.name} has died because you failed to take care of it properly.")
        pet.alive = False


    def play(self):
        if not self.alive:
            print(f"{self.name} is dead.")
            return
        
        while True:
            self.show_inventory()

            user_input = input('\nPick the number of the toy you want to select or type "exit" to go back: ')
            
            if user_input.lower() == "exit":
                break
            try:
                item_index = int(user_input) - 1

                item_picked = self.inventory[item_index]
                if item_picked.type == "toy":
                    self.thirst -= item_picked.effect
                    self.inventory.pop(item_index)
                    print(f"\n{self.name}'s happiness has increased by {self.happiness} after playing with {item_picked.name}")
            except ValueError:
                print('Please enter a valid number or type "exit" to return.')
    def gotcha(self):
        print("Current inventory:")
        self.show_inventory()
        
        user_input = input("\nEnter the number of the item you wish to select: ")
        user_index = int(user_input) -1
        
        item_picked = self.inventory[user_index]
        if item_picked.type == "egg":
            print("Hatching your egg...")
            time.sleep(3)
        
        breeds = {
            "Common": [
                breed("dog", ["loyal"], income_bonus=1.2, happiness_increase=1.2),
                breed("cat", ["independent"], income_bonus=1.1, hunger_decay=0.9)
                ],
            
            "Rare": [
                breed("wolf", ["wise"], income_bonus=1.5),
                breed("phoenix", ["fiery"], income_bonus=1.5, hunger_decay=0.8)
                ],
            "Legendary": [
                breed("hydra", ["acceptional strength"], income_bonus=2, hunger_decay=0.6)
                ],
            "Ultra Rare": [
                breed("dogoo", ["crazy buffs"], income_bonus=5, happiness_increase=2, hunger_decay=0.5),
            ]
        }
        
        rarity = None

        for rarity_type in breeds.keys():
            if rarity_type in item_picked.name:
                rarity = rarity_type
                break

        if not rarity:
            rarity = "Common"

        new_breed = random.choice(breeds[rarity])

        self.breed = new_breed

        print(f"Congratulation! Your egg hatched into a {new_breed.name}!")
        print(f"Traits: {new_breed.traits}")
        print(f"Income bonus: {new_breed.income_bonus}")

        if new_breed.happiness_increase != 1:
            print(f"Happiness bonus: {new_breed.happiness_increase}")
        if new_breed.hunger_decay != 1:
            print(f"Hunger Reduction: {new_breed.hunger_decay}")

    def money(self):
        print(f"You currently have ${self.money} in spending cash.")
    
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

    def shop(self):
        print("\nWelcome to the shop!")
         
        stored_items = {
            "1": {"name": "Pancake", "type": "food", "effect": 4, "price": 5},
            "2": {"name": "Waffle", "type": "food", "effect": 5, "price": 6},
            "3": {"name": "Burger", "type": "food", "effect": 8, "price": 10},
            "4": {"name": "Toy Ball", "type": "toy", "effect": 4, "price": 6},
            "5": {"name": "Toy Hammer", "type": "toy", "effect": 5, "price": 7},
            "6": {"name": "Frisbee", "type": "toy", "effect": 6, "price": 8},
            "7": {"name": "Water", "type": "liquid", "effect": 3, "price": 4},
            "8": {"name": "Apple Juice", "type": "liquid", "effect": 4, "price": 5},
            "9": {"name": "Egg (Common)", "type": "egg", "effect": None, "price": 8},
            "10": {"name": "Egg (Rare)", "type": "egg", "effect": None, "price": 15},
            "11": {"name": "Egg (Legendary)", "type": "egg", "effect": None, "price": 30},
            "12": {"name": "Egg (Ultra Rare)", "type": "egg", "effect": None, "price": 100}
        }


        while True:
            print(f"\nThe amount in your savings: ${self.money}")

            print("\nAvailable items:")
            for num, item_info in stored_items.items():
                name = item_info["name"]
                price = item_info["price"]
                effect = item_info["effect"]

                if effect is not None:
                    effect_text = f" (Effect: {effect})" 
                else:
                    effect_text = ""
                print(f"{num}. {name} - ${price}{effect_text}")

            print(f'\nEnter the number of the item you would like to buy, or type "exit" if you wish to leave.')
            user_input = input("\nEnter command here: ")

            if user_input.lower() == "exit":
                print("Bye, bye!")
                return
            
            if user_input in stored_items:
                item_info = stored_items[user_input]
                price = item_info["price"]

                if self.money >= price:
                    self.money -= price

                    new_item = item(
                        item_info["name"],
                        item_info["type"],
                        item_info["effect"]
                    )
                    self.inventory.append(new_item)
            
                    print(f"\n{new_item.name} has been added to your inventory! you now have ${self.money}.")

                    continue

user_name = input("Enter the name of your pet: ")
pet = tamagotchi(user_name) 

pet.auto_decay()
pet.auto_mood()

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
    print("4. Hatch eggs")
    print("5. Check status")
    print("6. Work a job")
    print("7. Shop")
    print("8. Exit")

    user_input = input("\nEnter the number of the thing you would like to do: ")

    if user_input == "1":
        pet.feed()
    if user_input == "2":
        pet.water()
    if user_input == "3":
        pet.play()
    if user_input == "4":
        pet.gotcha()
    if user_input == "5":
        pet.status()
    if user_input == "6":
        pet.job()
    if user_input == "7":
        pet.shop()
    if user_input == "8":
        print(f"Bye, bye! {pet.name} will be lonely without you.")
        break 


