import time
import random
import threading

class item:
    #Class for defining items. Type for if it is a toy, liquid, or a food item
    #as well as different effects they have i.e. +5 hunger. 
    def __init__(self, name, type, effect):
        self.name = name
        self.type = type
        self.effect = effect
        
    #Here is another class for defining a pets breed and the certain traits and buffs that the specific pet will give you.
class breed:
    def __init__(self, name, traits, income_bonus=1, hunger_decay=1, happiness_increase=1, strength_multiplier=1):
        self.name = name
        self.traits = traits
        self.income_bonus = income_bonus
        self.hunger_decay = hunger_decay
        self.happiness_increase = happiness_increase
        self.strength_multiplier = strength_multiplier
    
    #This is class is meant for keeping track of the pets stats such as hunger, thirst, happiness. As well as the inventory system and the player's money.
class tamagotchi:
    def __init__(self, name):
        self.name = name
        
        self.hunger = 9
        self.happiness = 1 
        self.thirst = 9
        self.money = 15
        self.inventory = []
        self.alive = True

        #Give the player some starter items.
        self.inventory.append(item("Pancake 🥞", "food", 5))
        self.inventory.append(item("Water 🚰", "liquid", 3))
        self.inventory.append(item("Toy Ball ⚽", "toy", 4))

        print("\nYou've received some starting items!")


    #While the player is in the game their pet's happines will slowely go down if they don't play with it, it's hunger and thirst will also increase 
    #and if it's hunger or thirst gets too high then the pet will unfortunately pass away😔. 
    def decay_overtime(self):
        while self.alive:
            time.sleep(175)
            self.hunger = min(20, self.hunger + self.breed.hunger_decay)
            self.thirst = min(20, self.thirst + self.breed.hunger_decay)
            self.happiness = max(0, self.happiness - self.happiness_increase)

            #Also add in the mood function that is down below for when the hunger, thirst, and happiness is updated to print the specific messages from the `mood` function.
            self.mood()

            if self.hunger >= 20:
                print(f"\n{self.name} has straved to death💀")
                self.die()
                break
            if self.thirst >= 20:
                print(f"\n{self.name} has died of dehydration💀")
                self.die()
                break

    #This is where we define a thread with the `decay_overtime` function as the base that will run in the background 
    #so that the pet's hunger and thirst will go down overtime whilst the game is being played.
    def auto_decay(self):
        decay_thread = threading.Thread(target=self.decay_overtime)
        decay_thread.daemon = True
        decay_thread.start()        

    #This one is basically self explanatory, but it displays the current inventory for the player.
    #We also start the indexing for the inventory at one so that it is a little easier for the end user.
    def show_inventory(self):
        if not self.inventory:
            print("\nYour inventory is empty")
            return
        
    
        print("\nInventory: ")
        for index, item in enumerate(self.inventory, 1):
            print(f"{index}. {item.name}")   
            

    #Function for displaying the current status of the pet.   
    def status(self):
    
        print(f"{self.name}'s stats:")
        print(f"Hunger: {self.hunger}"), 
        print(f"Happiness: {self.happiness}") 
        print(f"Thirst: {self.thirst}")
        print(f"Money: {self.money}")
        
    #This function will be running in the background inside the `decay_overtime` function to alert the user when their pet is hungery or thirsty or in a bad mood.
    def mood(self):
        if self.hunger >= 15:
            print(f"\n{self.name} is starving🍖😟")
        if self.thirst >= 15:
            print(f"\n{self.name} is dehydrated🥤😟")
        if self.happiness >= 10:
            print(f"\n{self.name} is happy😊")
        if self.happiness >= 6:
            print(f"\n{self.name} is neutral😐") 
        if self.happiness >= 3:
            print(f"\n{self.name} is sad 😢")
        print(f"\n{self.name} is in a very bad mood 😤")
        
        
        if self.happiness <= 4:
            self.hunger_decay = 5


    #Much like the name suggests this is the function where the player can feed their pet.
    def feed(self):

        while True:
            #Show the inventory so that the user can pick the number of the food item they want to give to thier pet.
            self.show_inventory()
            user_input = input('\nPick the number of the food you would like to select or type "exit" to go back: ')

            if user_input.lower() == "exit":
                break

            try:
                
                #Start the count at 1 since it is easy for the user.
                item_index = int(user_input) - 1

                #The selected item is whatever the index of the item is from the inventory defined in the `tamagotchi` class.
                selected_item = self.inventory[item_index]

                #If the type of item is defined as "food" then we know it's food and it can be given to the pet
                if selected_item.type == "food":

                    #We define that the hunger cannot go below 0 and then we minus the effect of the selected item from the current hunger of the pet.
                    self.hunger = max(0, self.hunger - selected_item.effect)
                    self.inventory.pop(item_index)
                    print("\n===========================================================================================")
                    print(f"{self.name} has been feed with {selected_item.name}. Their hunger is now at {self.hunger}.")
                    print("===========================================================================================")
                else:
                    print("\n================")
                    print("Not a food item!")
                    print("================")

            except ValueError:
                print("\n===========================================================================================")
                print('Please enter a valid number or "exit" to go back.')
                print("===========================================================================================")
       

    #Honestly the almost the exact same thing happens here as in the feed function it is just with liquids instead of food.
    def water(self):

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
                    print("\n===================================================================================")
                    print(f"{self.name} has been given {selected_item.name}. Their thirst is now {self.thirst}.")
                    print("===================================================================================")
                else:
                    print("\n=================")
                    print("Not a liquid!")
                    print("=================")
                    
            except ValueError:
                print("\n=====================================================")
                print('Please enter a valid number or type "exit" to return.')
                print("=====================================================")
                
    #This is a function that just sets the alive status defined in the `tamagotchi` class to false so that we can call it when needed.
    def die(self):
        
        self.alive = False

    #The same function as the other two but this time it is for playing with your pet.
    def play(self):
        
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
                    print("\n================================================================================================")
                    print(f"{self.name}'s happiness has increased by {self.happiness} after playing with {item_picked.name}")
                    print("================================================================================================")
                else:
                    print("\n==========")
                    print("Not a toy!")
                    print("==========")
            except ValueError:
                print("\n=====================================================")
                print('Please enter a valid number or type "exit" to return.')
                print("=====================================================")
        


    #Once the player buys an egg this function allows them to hatch their egg and based on the egg they can either get a 
    #common, rare, legendary, or ultra rare pet.
    def gotcha(self):

        print("Current inventory:")
        self.show_inventory()
        
        user_input = input("\nEnter the number of the item you wish to select: ")
        
        try:
        
            #Convert the user input into an integer and start the count at one.    
            user_index = int(user_input) -1
                
            #Get the selected item from the users inventory.
            item_picked = self.inventory[user_index]

            #Check if the item is an egg. If not give an error.
            if item_picked.type == "egg":
                print("\n----------------------->")
                print("Hatching your egg...")
                print("----------------------->")
                time.sleep(3)
            else:
                print("\nThis item is not an egg. Please select an egg.")
                time.sleep(1.5)
                return
        
            #Define the different breeds and their rarities.
            breeds = {
                "Common": [
                    breed("dog", ["Loyal"], income_bonus=1.2, happiness_increase=1.2),
                    breed("cat", ["Independent"], income_bonus=1.1, hunger_decay=0.9),
                    breed("Hamster", ["Tiny", "Playful"], income_bonus=1.0, hunger_decay=1.0, happiness_increase=1.0),
                    breed("Guinea Pig", ["Social", "Curious"], income_bonus=1.1, happiness_increase=1.2, hunger_decay=1.1)
                    ],
                
                "Rare": [
                    breed("Chinchilla", ["Fluffy", "Energetic"], income_bonus=1.3, happiness_increase=1.5, hunger_decay=.7),
                    breed("Wolf", ["wise"], income_bonus=1.5),
                    breed("Phoenix", ["fiery"], income_bonus=1.5, hunger_decay=0.8)
                    ],
                "Legendary": [
                    breed("Hydra", ["Powerful", ""], income_bonus=2, hunger_decay=0.6),
                    breed("Dragon", ["Majestic", "Powerful"], income_bonus=2.5, happiness_increase=1.5, hunger_decay=.6),
                    breed("Chupacabra", ["Quick-Witted", "Minimilistic"], income_bonus=2, happiness_increase=1.2, hunger_decay=.4)
                    ],
                "Ultra Rare": [
                    breed("Dogoo", ["crazy buffs"], income_bonus=10, happiness_increase=2, hunger_decay=0.5),
                    breed("Chimera", ["Mythical", "Fierce"], income_bonus=5.5, hunger_decay=0.45, happiness_increase=2)
                ]
            }
            
            rarity = None

            #Determine the rarity of the egg
            for rarity_type in breeds.keys():
                if rarity_type in item_picked.name:
                    rarity = rarity_type
                    break

            #randomly select a random breed from the rarity category.
            new_breed = random.choice(breeds[rarity])

            #Assign the new breed.
            self.breed = new_breed

            print(f"\nCongratulation! Your egg hatched into a {new_breed.name}!")
            print(f"Traits: {new_breed.traits.strip()}")
            print(f"Income bonus: {new_breed.income_bonus}")
            time.sleep(1.5)

            #If the happiness bonus or hunger decay aren't at the defualt then display the bonuses. 
            if new_breed.happiness_increase != 1:
                print(f"\nHappiness bonus: {new_breed.happiness_increase}")
            if new_breed.hunger_decay != 1:
                print(f"\nHunger Reduction: {new_breed.hunger_decay}")

        except ValueError:
            print("\nPlease enter a valid command.")
            time.sleep(1.5)

    #Tell the user how much money they currently have.
    def money(self):
        print(f"You currently have ${self.money} in spending cash.")


    def job(self):

        #The player can choose between two jobs to perform to make some money.
        print("\nWhich job would you like to perform?")
        print("\n1. Picking up trash - 2 dollars per piece of trash")
        print("2. Look for change under vending machines - 1 to 5 dollars based on the vending machine")
        
        user_input = input("\nEnter the number of the job you would like to perform: ")

        #Create a variable to pick a random number between one and five, for when the user chooses to go the looking for change route.
        num = random.randint(1, 5)
        

        if user_input == "1":
            base_earnings = 2

            #Multiple the base_earnings of the job by the income_bonus of the certain breed of pet the user has.
            earnings = int(base_earnings * self.breed.income_bonus)
            print("Picking up trash...")
            time.sleep(5)
            self.money += 2
            print("You earned 2 dollars!")
            time.sleep(1.5)
        elif user_input == "2":
            base_earnings = num
            earnings = int(base_earnings * self.breed.income_bonus)
            print("Looking for change...")
            time.sleep(10)
            self.money += num
            print(f"You earned {num} dollars from looking for change!")
            time.sleep(1.5)
        else:
            print("\nInvalid input. Please enter a valid option.")

    def shop(self):

        #Let the player purchase items and eggs from the shop.
        print("\nWelcome to the shop!🏪")
         
        #the avaliable items in the shop.
        stored_items = {
            "1": {"name": "Pancake 🥞", "type": "food", "effect": 4, "price": 5},
            "2": {"name": "Waffle 🧇", "type": "food", "effect": 5, "price": 6},
            "3": {"name": "Burger 🍔", "type": "food", "effect": 8, "price": 10},
            "4": {"name": "Toy Ball ⚽", "type": "toy", "effect": 4, "price": 6},
            "5": {"name": "Toy Hammer 🔨", "type": "toy", "effect": 5, "price": 7},
            "6": {"name": "Frisbee 🥏", "type": "toy", "effect": 6, "price": 8},
            "7": {"name": "Water 🚰", "type": "liquid", "effect": 3, "price": 4},
            "8": {"name": "Apple Juice 🧃", "type": "liquid", "effect": 4, "price": 5},
            "9": {"name": "Egg (Common)🥚", "type": "egg", "effect": None, "price": 8},
            "10": {"name": "Egg (Rare) 🥚", "type": "egg", "effect": None, "price": 15},
            "11": {"name": "Egg (Legendary) 🥚", "type": "egg", "effect": None, "price": 30},
            "12": {"name": "Egg (Ultra Rare)🥚", "type": "egg", "effect": None, "price": 100}
        }

        #Shop loop so the user stays inside the shop until they decide to exit.
        while True:

            #show the player how much money they have.
            print(f"\nAmount in your savings: ${self.money}")

            print("\nAvailable items💰:")
            
            for num, item_info in stored_items.items():
                name = item_info["name"]
                price = item_info["price"]
                effect = item_info["effect"]

                #Format the display text.
                if effect is not None:
                    effect_text = f" (Effect: {effect})" 
                else:
                    effect_text = ""
                print(f"{num}. {name} - ${price}{effect_text}")


            #Tell the player to make a selection or leave the shop.
            print(f'\nEnter the number of the item you would like to buy, or type "exit" if you wish to leave.')
            user_input = input("\nEnter command here: ")

            #If the player types "exit" then exit the shop.
            if user_input.lower() == "exit":
                print("Bye, bye!")
                return
            
            #Proccess their selection
            if user_input in stored_items:
                item_info = stored_items[user_input]
                price = item_info["price"]

                #Check if they have the money if they do then subtract from their money the price of the item.
                if self.money >= price:
                    self.money -= price

                    #Create the new item and then add it to their inventory.
                    new_item = item(
                        item_info["name"],
                        item_info["type"],
                        item_info["effect"]
                    )

                    #Append the new item to their inventory.
                    self.inventory.append(new_item)
                    print("\n====================================================================")
                    print(f"{new_item.name} has been added to your inventory! you now have ${self.money}.")
                    print("====================================================================")
                    time.sleep(2.5)
                    continue