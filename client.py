
import socket 
import threading

def connect_server():
    
    global client    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect("localhost", 5000)
    print("Connected to the server")
    
    return client

def server_messages(client, command):
    
    try:
        while True:
            
            message = client.recv(1024).decode()
            if message:
                print(f"\nServer: {message}")
            
    except:
        print("Lost connection.")
        
    
def handle_requests():
        
    other_player = input("Enter the IP address of the other player: ")
    
    client.send(f"REQUEST|{other_player}").encode()
    
    response = client.recv(1024).decode()
    
        
        
def multiplayer(pet):

    connect_server()
    
    listener = threading.Thread(target=server_messages, daemon=True)
    listener.start()

    
    while True:
        command = input('Enter a command or type "exit" to leave multiplayer: ')
        if command.lower() == "exit":
            print("Leaving multiplayer")
            client.close()
            break
        client.send("ACTION|{command}").encode()