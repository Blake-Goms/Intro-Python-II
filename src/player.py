# Write a class to hold player information, e.g. what room they are in
# currently.

# instructor said should be 4 lines of code... got it!


class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"\nYou picked up {item.name}.\n")

    def drop_items(self, item):
        self.current_room.items.append(item)
        self.items.remove(item)


''' LECTURE DAY 2

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        # player has attr current_room
        self.current_room = starting_room

    def travel(self, direction):
        # player should be to move in a direction
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction")
'''
