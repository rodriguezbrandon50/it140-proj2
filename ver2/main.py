# Brandon Rodriguez

def display_move_keys():
    print('MOVEMENT: W -> UP A -> LEFT S -> DOWN D -> RIGHT    R -> INTERACT')
    
def show_player_status():
    print('room name placeholder')
    print('inventory placeholder')
    print('item in this room placeholder')
    
def main_menu():
    # display main menu and commands
    # display game title
    print('GAME NAME')
    print('win cond: purpose of game')
    print('lose cond: how you lose')
    
def lose_screen():
    pass

def win_screen():
    pass    

def run_intro():
    main_menu()
    display_move_keys()
        
    
    
def main():
    # Player inventory is an empty list
    # Will append inventory items as they are collected
    player_inventory = []
    
    # These flags will be used to determine how the game
    # ends. They are checked at multiple points in the game
    flag_game_end = False # triggers exit of main loop
    flag_win_game = False # triggers after inventory has all items
    flag_lose_game = False # triggers if an enemy is encountered
    
    tower = {
    'floor 1': {
        'center': 'The Waiting Room of Despair',
        'Room 1': 'Empty desk and a chair. You hear shuffling behind you.',
        'Room 2': 'Green Gem of Wisdom',
        'Room 3': 'John the Green Viper found out you do not have an appointment.\nHe kills you with a stapler.',
        'Room 4': 'Just a bunch of documents in boxes. You hear movement coming from inside the boxes.'
    },
    'floor 2': {
        'center': 'Hell\'s Kitchen',
        'Room 1': 'Enemy',
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
        'Room 4': 'Soulstone found'
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
