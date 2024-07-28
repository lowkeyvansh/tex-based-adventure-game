def introduction():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. Your goal is to find the hidden treasure.")
    print("Be careful of the dangers that lurk in the forest!")

locations = {
    "forest": {"description": "You are in a dark, dense forest.", "north": "cave", "east": "lake"},
    "cave": {"description": "You are in a dark cave. You hear something moving.", "south": "forest"},
    "lake": {"description": "You are by a serene lake. You see something shiny in the water.", "west": "forest"}
}

player_location = "forest"

def move_player():
    global player_location
    direction = input("Which direction do you want to go? (north/south/east/west) ").strip().lower()
    if direction in locations[player_location]:
        player_location = locations[player_location][direction]
    else:
        print("You can't go that way.")

def search_location():
    global player_location
    if player_location == "lake":
        print("Congratulations! You found the hidden treasure in the lake!")
        exit()
    elif player_location == "cave":
        print("Oh no! A monster caught you! Game over.")
        exit()
    else:
        print("You found nothing of interest.")

def game_loop():
    while True:
        location = locations[player_location]
        print(location["description"])
        action = input("What do you want to do? (move/search/quit) ").strip().lower()
        
        if action == "quit":
            print("Thanks for playing!")
            break
        elif action == "move":
            move_player()
        elif action == "search":
            search_location()
        else:
            print("Invalid action. Try again.")

if __name__ == "__main__":
    introduction()
    game_loop()
