from room import Room
from player import Player
# Declare all the rooms

room = {
    # Room(argument 1/name, argument 2/description)
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Player class requires name and current room


def play_game():
    global player
    print('You are currently at, ', {player.current_room})
    location = input("Where would you like to go next? ")
    if location == "n":
        player.current_room = player.current_room.n_to

    elif location == "s":
        player.current_room = player.current_room.s_to

    elif location == "e":
        player.current_room = player.current_room.e_to

    elif location == "w":
        player.current_room = player.current_room.w_to
    elif location == "q":
        print("Thanks for playing, Goodbye!")
        quit()
    else:
        print('Thats not a nesw key! You lost your sense of direction. You lose! ')
        quit()


name = input("Enter your gamertag: ")
print(f'Welcome to your virtual game, {name}')
print("Navigate the game using nesw keys! To quit press q")
# assign the gamertag
player = Player(name)
# assign to dict room outside
player.current_room = room['outside']


isPlaying = True
while isPlaying:
    play_game()

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# While loop will execute until function quits


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
