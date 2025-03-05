import socket

#Create a socket object for the server.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Make the host be any IP address with 0.0.0.0 and bind it to port 5000.
server.bind(("0.0.0.0", 5000))

#Listen for connections.
server.listen(1)
print("Listening for connections...")


client, address = server.accept()
print("Connection from: " + str(address))

while True:

    #Decode the message from the client.
    data = client.recv(1024).decode()
    print(f"Received: {data}")
    
    if not data:
        break

    #Split the data at the pipe to get the user input. 
    item = data.split("|")
    
    #If the first thing in the message from the client is "INPUT" then we know that it's right 
    #then we take the second piece to that message which will be the user input that represented by index 1 and will be assigned to the `command` variable.
    if item[0] == "INPUT":
        command = item[1].strip()
    
        #Depending upon the input from the user we will send an encoded message back to the client that corresponds to the action they want to take.
        if command == "1":
            client.send("feed".encode())
        if command == "2":
            client.send("water".encode())
        if command == "3":
            client.send("play".encode())
        if command == "4":
            client.send("gotcha".encode())
        if command == "5":
            client.send("status".encode())
        if command == "6":
            client.send("job".encode())
        if command == "7":
            client.send("shop".encode())
        if command == "8":
            client.send("exit".encode)
        if command.lower() == "help":
            client.send("help".encode())


        
        
    
    
