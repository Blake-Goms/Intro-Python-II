from room import Room
from player import Player
from item import Item
# player is name of file. Player is name of Class
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

# List of items
hammer = Item(
    'Mjolnir', 'Whosoever holds this hammer, if he be worthy, shall possess the power of Thor.')
spear = Item('Gungnir', ' Spear of the All-Father, Odin, King of Asgard')
sword = Item(
    'Hofund', 'Sword of the Vanir God, Heimdall, protector of the Bifrost')

# Add items to rooms
room['treasure'].add_item(hammer)
room['overlook'].add_item(spear)
room['foyer'].add_item(sword)


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
    print('You are currently at, ', player.current_room)

    # For Exploring items
    explore = input("Search the room for Items? Enter [y] or [n] ~~> ")
    if explore == 'y':
        if len(player.current_room.items) > 0:
            print(
                f'You found a legendary item!\n {player.current_room.items[0].name, player.current_room.items[0].description } \n')
            pickup_item = input(
                "\nWould you like take this item? Enter [y] or [n] ~~> ")
            if pickup_item == 'y':
                player.add_item(player.current_room.items[0])
                print('\n Here are the items in your inventory:\n',
                      player.items, '\n')
                choice = input(
                    '\nWould you like to remove any item in the inventory? Enter [y] or [n]:\n')
                if choice == 'y':
                    selected_item = input('\nEnter Item Name:\n')
                    # if remove == 'Mjolnir' or 'Gungnir' or 'Hofund':
                    #     player.drop_items(choice)
                    for x in player.items:
                        if selected_item in player.items:
                            player.drop_items(selected_item)
                            print(f'\n You have dropped: {selected_item}\n')

    elif explore == 'q':
        print("\nThanks for playing, Goodbye!\n")
        quit()
    else:
        pass

    # For Location
    location = input("\nWhere would you like to go next? \n")
    if location == "n":
        player.current_room = player.current_room.n_to

    elif location == "s":
        player.current_room = player.current_room.s_to

    elif location == "e":
        player.current_room = player.current_room.e_to

    elif location == "w":
        player.current_room = player.current_room.w_to
    elif location == "q":
        print("\nThanks for playing, Goodbye!\n")
        quit()
    else:
        print(
            '\nThats not a [n],[e],[s],[w] key! You lost your sense of direction. You lose! \n')
        quit()


name = input("Enter your gamertag: ")
print(f'\nWelcome to your virtual game, {name}\n')
print("\nNavigate the game using [n],[e],[s],[w] keys! To quit press [q] \n")
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

''' LECTURE DAY 2

player = Player(input("Please enter name: "), room['outside'])
print(player.current_room)
directions = ["n", "s", "e", "w"]

while True:
    cmd = input("~~> ")
    if cmd in directions:
        # Make player travel in that direction
        player.travel(cmd)
    elif cmd == "q":
        print("Bye")
        break
    else:
        print("I did not recognize that")

'''
