
import socket 
import tamagotchi

def connect_server():
    
    #Create a socket object.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connect to the localhost on port 5000.
    client.connect(("localhost", 5000))
    print("Connected to the server")
    
    return client

client = connect_server()

#Prompt the user to give the pet a name.
user_name = input("Enter the name of your pet: ")
pet = tamagotchi.tamagotchi(user_name) 

#Create a help function incase the player wants to display information about the game incase the uesr wants to learn more about the game.
def help():
    print("===========INFORMATION==============")
    print("In this game you care for a virtual pet.")
    print("You can feed, water, and play with the pet.")
    print("Buy items from the shop to give to your pet.")
    print("Or buy eggs from the shop and hatch them for new pets with different buffs.")
    print("Work jobs to make money.")
    print("Type in the number associated with the thing you would like to select to get started.")
    print("====================================")

#While the pet is actually alive print the options for playing the game.
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


    user_input = input("\nEnter the number of the item you would like to select: ")

    #Send a message to the server with the "INPUT" from the user and make sure to add the word input at the beginning seperated from the actual input so that the server can Identify what the actual input is.
    client.send(f"INPUT|{user_input}".encode())
    
    #Once the server has gotten the "INPUT" we sent and sent back a message back we can decode that information. 
    message = client.recv(1024).decode()

    #Depending on what the user input the server will send back a message in correlation to the specific action to be performed.
    if message == "feed":
        pet.feed()
    if message == "water":
        pet.water()
    if message == "play":
        pet.play()
    if message == "gotcha":
        pet.gotcha()
    if message == "status":
        pet.status()
    if message == "job":
        pet.job()
    if message == "shop":
        pet.shop()
        
    if message == "exit":
        print(f"Bye, bye! {pet.name} will be lonely without you.")
        break
    
    #Run the help function if they want to display information about the game.
    if message == "help":
        help()
        
    
    
