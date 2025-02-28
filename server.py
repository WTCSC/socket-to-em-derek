import socket
import threading 
import random


breeds = {
    "Dog": ["Loyal", "Energetic"],
    "Cat": ["Independent", "Curious"],
    "Hydra": ["Acceptional Strength", "Three heads"],
    "Phoenix": ["Rebirth", "Fiery"],
    "Wolf": ["Alpha", "Wise"]

}

def breed_pets(pet1, pet2):
    new_pet_name = f"{pet1['name']}-{pet2['name']} Jr."

    new_traits = random.sample(pet1["traits"], 1) + random.sample(pet2["traits"], 1) 

    if pet1["breed"] ==pet2["breed"]:
        new_breed = pet1["breed"]
    else:
        new_breed = f"{pet1['name']}-{pet2['name']} Jr."

    new_pet = {
        "name": new_pet_name, 
        "breed": new_breed,
        "traits": new_traits,
        "hunger": (pet1["hunger"] + pet2["hunger"]) // 2,
        "thirst": (pet1["thirst"] + pet2["thirst"]) // 2,
        "happiness": (pet1["happiness"] + pet2["happiness"]) // 2
    }

    return new_pet



def client_connections(client, addr):
    print(f"Connnected to {addr}")

    while True:
        data = client.recv(1024).decode()
        if not data:
            break
    
    
