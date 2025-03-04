
import socket 
import tamagotchi

def connect_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5000))
    print("Connected to the server")
    
    return client

client = connect_server()

user_name = input("Enter the name of your pet: ")
pet = tamagotchi.tamagotchi(user_name) 

pet.auto_decay()
pet.auto_mood()

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
    
    tamagotchi.inventory.append("Pancake", "food", 5)

    user_input = input("\nEnter the number of the item you would like to slect: ")
    client.send(f"INPUT|{user_input}".encode())
    
    message = client.recv(1024).decode()

    if message == "feed":
        pet.feed()
    # if user_input == "2":
    #     pet.water()
    # if user_input == "3":
    #     pet.play()
    # if user_input == "4":
    #     pet.gotcha()
    # if user_input == "5":
    #     pet.status()
    # if user_input == "6":
    #     pet.job()
    # if user_input == "7":
    #     pet.shop()
        
        
    # if user_input == "8":
    #     print(f"Bye, bye! {pet.name} will be lonely without you.")
    #     break
    
    
    
