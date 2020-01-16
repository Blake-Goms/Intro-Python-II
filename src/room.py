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

    def __repr__(self):
        return f' Name: {self.name}, Description: {self.description}'
        # repr is for development environment, stack overflow

    def __str__(self):
        # str is for production environment, stack overflow
        return f'Name: {self.name}, Description: {self.description}'
