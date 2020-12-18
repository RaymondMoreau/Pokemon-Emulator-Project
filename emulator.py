#####################
# Raymond and Ashton's Pokemon Emulator
#####################

class Pokemon():
    """Pokemon class"""
    def __init__(self, name="None", t="None", level=0):
        """Override of initialization for the Pokemon"""
        self.name = name
        self.type = t
        self.level = level
        self.health = 10

    def __repr__(self):
        """Override of print function for Pokemon class"""
        return "Level " + str(self.level) + " " + self.name + ". " + self.type + " type."