import os 

# we can use this function to clear the screen
# if os is windows use cls else use clear (linux/iOS)
def cls_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def display_player_state(floor_check, player):
    print(f"You are on floor {floor_check}")
    print(f"You have {len(player.inventory)}") 
    
