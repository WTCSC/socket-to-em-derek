import socket
import threading 

player_pets = {}

server = socket.socket(socket.AF_NET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))

server.listen(1)
print("Listening for connections...")

def handle_connections(client, addr):
    
    print(f"Connnected to {addr}")

    while True:
        data = client.recv(1024).decode()
        if not data:
            break
        data = data.split("|")
        command = data[0]
        
        
        
    
        
        
    
    
