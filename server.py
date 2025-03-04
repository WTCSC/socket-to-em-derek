import socket

money = 20

player_inventory = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))

server.listen(1)
print("Listening for connections...")

client, address = server.accept()
print("Connection from: " + str(address))

while True:
    data = client.recv(1024).decode()
    print(f"Received: {data}")
    
    if not data:
        break
    item = data.split("|")
    
    if item[0] == "INPUT":
        command = item[1].strip()
    
        if command == "1":
            client.send("feed".encode())



        
        
    
    
