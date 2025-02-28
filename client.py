
import socket 
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect('localhost', 5000)
print("Connected to the server")

def register_pet(pet):
    client.send(f"PET"|{pet.name}|{pet.breed}|{pet.hunger}|{pet.thirst}|{pet.happiness})
    print(client.recv(1024).decode())
    
def server_messages(pet):
    
    try:
        while True:
            
            message = client.recv(1024).decode()
            if message:
                print(f"\nServer: {message}")
            
    except:
        print("Lost connection.")
        
def multiplayer(pet):
    
    register_pet(pet)
    listener = threading.Thread(target=server_messages, daemon=True)
    listener.start()

    
            
        
    