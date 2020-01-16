# Implement a class to hold room information. This should have name and
# description attributes.

# prob 20-40 lines


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.w_to = None
        self.e_to = None
        self.s_to = None
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __repr__(self):
        return f' \n----------------\n\nName: {self.name}, Description: {self.description} \n \n----------------\n'
        # repr is for development environment, stack overflow

    def __str__(self):
        # str is for production environment, stack overflow
        return f'\nName: {self.name}, Description: {self.description} \n'


''' LECTURE DAY 2

class Room:
    def __init__(self, name, description):
        # Name, description
        self.name = name
        self.description = description
        # n_to, s_to, e_to, w_to
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        display_string = ""
        display_string += f"\n----------------\n"
        display_string += f"\n{self.name}\n"
        display_string += f"\n{self.description}\n"
        display_string += f"\n{self.get_exits_string()}\n"
        return display_string

    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None

    def get_exits(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits

    def get_exits_string(self):
        return f"Exits: {', '.join(self.get_exits())}"
'''
