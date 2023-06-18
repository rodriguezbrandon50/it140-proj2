# Brandon Rodriguez
import os

def game_key():
    gk = [(2,3), (3,1), (1,4), (4,2), (1,2), (2,3), (3,1), (1,4)]
    return gk

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def display_win_screen():
    print('C O N G R A T S   Y O U   B E A T   T H E   L A S T   B O S S')

def display_lose_screen():
    print('Y O U  L O S E')
    
def display_move_keys():
    print('MOVEMENT: W -> UP A -> LEFT S -> DOWN D -> RIGHT    R -> INTERACT')
    
def show_player_status(floor_dict, inv_list, floor_count):
    # gets value from 'center' in floor_dict
    print(f"You are in room {floor_dict['center']} on floor {floor_count}")
    print(f"You have {len(inv_list)} gems in your inventory. You need { (8 - len(inv_list)) }")
    
    # gem on this floor
    key = game_key()
    floor_key = key[floor_count - 1]
    gem_name = floor_dict[f'Room {floor_key[0]}']
    print(f'You need to find the {gem_name}')

def main_menu():
    # display main menu and commands
    # display game title
    print('FROG KNIGHT')
    print('win cond: Collect all gems to restore Frog knight\'s power.')
    print('lose cond: Frog Knight is in a weakened state. Encountering enemies is lethal.')

def check_win_lose(win_flag, lose_flag):
    if win_flag is True and lose_flag is False:
        display_win_screen()
        input('PRESS ANY KEY TO EXIT')
        exit()
    elif win_flag is False and lose_flag is True:
        display_lose_screen()
        input('PRESS ANY KEY TO EXIT')
        exit()
    else:
        print('FLAG READING ERROR')

def run_intro():
    main_menu()
    display_move_keys()
    input('PRESS ENTER TO CONTINUE')
    clear_screen()

def get_player_input():
    good_in = False
    
    while good_in is False:
        player_in = input('Which room do you want to go to? ')
        player_in = player_in.strip()
        player_in = player_in.lower()
        player_in = player_in[0]
        
        if any(char == 'w' or char == 'a' or char == 's' 
               or char == 'd' for char in player_in):
            good_in = True
        else:
            print('\nPlease input correct value')
            display_move_keys()
            good_in = False

    if player_in == 'w':
        return ('Room 1', 1)
    elif player_in == 's':
        return ('Room 2', 2)
    elif player_in == 'a':
        return ('Room 3', 3)
    elif player_in == 'd':
        return ('Room 4', 4)
    else:
        print('invalid input in move to function')
        return 'invalid'

# This was going to be used to have player 'pick up' item
# Made this automatic instead
#def interact(inventory, room):
#    good_inp = False
#    
#    while good_inp is False:
#        input('Press r to add gem to inventory: ')
#        
#        if input.lower() == 'r':
#            inventory.append()
    
def main():
    # Player inventory is an empty list
    # Will append inventory items as they are collected
    player_inventory = []
    
    # These flags will be used to determine how the game
    # ends. They are checked at multiple points in the game
    flag_game_end = False # triggers exit of main loop
    flag_win_game = False # triggers after inventory has all items
    flag_lose_game = False # triggers if an enemy is encountered
    
    floor_counter = 1

    tower = {
    'floor 1': {
        'center': 'The Waiting Room of Despair',
        'Room 1': 'You see an empty desk and a chair. You hear shuffling behind you.',
        'Room 2': 'Green Gem of Wisdom',
        'Room 3': 'John the Green Viper found out you do not have an appointment.\nHe kills you with a stapler.',
        'Room 4': 'Just a bunch of documents in boxes. You hear movement coming from inside the boxes.'
    },
    'floor 2': {
        'center': 'Hell\'s Kitchen',
        'Room 1': 'Pit Viper Gordoram the BBQ pit master throws you into the smoker. You cook to perfection.',
        'Room 2': 'Piles of room temperature meat cover the ground. It smells vile in here.\n You hear faint cries of sorrow.',
        'Room 3': 'Red Gem of Valor',
        'Room 4': 'Bones litter the ground. The vile smell repulses you.'
    },
    'floor 3': {
        'center': 'Forge of Hatred',
        'Room 1': 'Blue Gem of Serenity',
        'Room 2': 'Empty workshop. A breeze makes your hair stand. It felt like a warmth breath. You are alone. ',
        'Room 3': 'Tools line the walls in this room.\n The smell of blood fills your nostrils.',
        'Room 4': 'Enemy'
    },
    'floor 4': {
        'center': 'Supply Storage of Disorder',
        'Room 1': 'You find a dead body with a to do checklist. \nJames the intern. \nPiles of office supplies partially cover his remains.',
        'Room 2': 'Enemy',
        'Room 3': 'Empty storage room. Deep discomfort fills your belly.',
        'Room 4': 'Soulstone'
    },
    'floor 5': {
        'center': 'Server Room of Bad Cable Management',
        'Room 1': 'White Gem of Stamina',
        'Room 2': 'You have encountered Jim the Boa Constrictor. He kills you with cat6e cable.',
        'Room 3': 'Its just a bunch of machines. You see cables littering the ground. Its warm.',
        'Room 4': 'Just a bunch of machines. You hear faint beeping. You feel eyes on you.'
    },
    'floor 6': {
        'center': 'Dormitory of Unrest',
        'Room 1': 'Empty beds line this room. They must all be on the clock.',
        'Room 2': 'Yellow Gem of Speed',
        'Room 3': 'Kyle the micromanager finds you. \nYou are given your final write up for resting on the clock. \nKyle fires you from life.',
        'Room 4': 'Empty beds line this room. They must all be on the clock.'
    },
    'floor 7': {
        'center': 'Workshop of Damnation',
        'Room 1': 'General Manager Gabe find you away from your station. \nYou are flogged and put to work.',
        'Room 2': 'You see a long assembly line. The workers do not notice your presence. \nYou feel a sense of despair loom over you.',
        'Room 3': 'Item',
        'Room 4': 'You see people strapped to chairs. Eyes forced open. \nThe sound of training videos fills the room.'
    },
    'floor 8': {
        'center': 'Office of Vice President Jason.',
        'Room 1': 'Gem of Salvation, this gem fills you with courage. \nWarm comfort fills your heart.',
        'Room 2': 'Various broken weapons litter this room. ',
        'Room 3': 'The remains of previous challengers are piled in this room. Numbness fills your heart.',
        'Room 4': 'VP Jason finds you. \nJason is a viper with a black belt. \nHe whoops your butt in a fight. '
    }
}

    run_intro()
 
    while flag_game_end is False:
        # get floor attributes
        if floor_counter < 9:    
            gem_found = False
            floor = f'floor {floor_counter}'
            current_floor = tower[floor]
        
        print('\n\n\n\n\n')
        
        # Tell player where they are at
        show_player_status(current_floor, player_inventory, floor_counter)
        display_move_keys()

        # this will hold the dictionary key needed in a tuple
        p_in = get_player_input()   # validates user input & returns key value 
        player_dictkey, player_movekey = p_in
        
        # key for the entire game
        key = game_key()    #gets list of tuples that contain gem/enemy locations
        
        # keys for this floor
        floor_key = key[floor_counter - 1] # this is because arrays start at 0
        gem_location, enemy_location = floor_key # (gem, enemy) tuple orientation

        if player_movekey == enemy_location:
            flag_lose_game = True
            enemy_text = current_floor[player_dictkey]
            print('You have encountered an enemy!')
            print(enemy_text)
            input('press any key to continue...')
            clear_screen()
            flag_game_end = True
        elif player_movekey == gem_location:
            flag_lose_game = False
            flag_game_end = False
            item_text = current_floor[player_dictkey]
            player_inventory.append(current_floor[player_dictkey])
            floor_counter += 1
            print(f'You found {item_text}!')
            print(f'Move on to floor {floor_counter}')
            clear_screen()
        else:
            print(current_floor[player_dictkey])
            flag_game_end = False
            clear_screen()

        if floor_counter == 9 and flag_lose_game is False and len(player_inventory) == 8:
            flag_win_game = True
            flag_game_end = True            

            
    clear_screen()
    check_win_lose(flag_win_game, flag_lose_game)
    input()
    exit()


if __name__ == '__main__':
    main()
