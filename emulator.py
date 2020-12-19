#####################
# Raymond and Ashton's Pokemon Emulator
#####################

class Pokemon:
    """Pokemon class"""

    def __init__(self, name="None", t="None", level=0, health=0):
        """Override of initialization for the Pokemon
        *Needs to be updated when new variables are added*

        Current variables attached to Pokemon:
        Name (str)
        Type (str)
        Level (int)
        Health (int)

        """
        self.name = name
        self.type = t
        self.level = level
        self.hp = health

    def __repr__(self):
        """Override of print function for Pokemon class
        *Needs to be updated when new variables are added*
        """
        return "Level " + str(self.level) + " " + self.name + ". " + self.type + " type. Current health: " + str(
            self.hp)

    def createpokemon(self):
        """Function called creating Pokemon
        *Needs to be updated when new variables are added*

        Current variables attached to Pokemon:
        Name (str)
        Type (str)
        Level (int)
        """
        name = input("What is the pokemons name?").strip().lower().capitalize()

        t = input("What is " + name + "'s type?").strip().lower().capitalize()

        check = True
        while check:
            # this system ensures pokemon level is a valid number (1-100)
            # will loop through until valid number is entered

            level = input("What is " + name + "'s level?").strip()

            try:  # tests for if input was an integer, if so, executes code.
                level = int(level)

                if level <= 0:  # test case for if input was equal to or below 0
                    print("Levels are a whole number from 1-100. It cannot be below 1. Please try again.")

                elif level > 100:  # test case for if input was above 100
                    print("Levels are a whole number from 1-100. It cannot be above 100. Please try again.")

                else:  # leaves loop if input is whole number from 1-100
                    check = False

            except ValueError:  # if value is not an integer, prints this message
                print("Level has to be a whole number from 1-100. Please try again.")

        check2 = True
        while check2:
            # this system ensures pokemon health is a valid number (0-infinity)
            # will loop through until valid number is entered

            health = input("What is " + name + "'s health?").strip()

            try:  # tests for if input was an integer, if so, executes code.
                health = int(health)

                if health <= 0:
                    print("Health has to be a whole number higher than 0. Please try again.")
                else:
                    check2 = False

            except ValueError:  # if value is not an integer, prints this message
                print("Health has to be a whole number higher than 0. Please try again.")

        self.name = name
        self.type = t
        self.level = level
        self.hp = health

        pass

    def takedamage(self, damage):
        """(Pokemon, int) --> None
        Pokemon, or self, takes damage."""

        self.hp -= damage

        pass

    def gainhealth(self, healing):
        """(Pokemon, int) -->
        Pokemon, or self, heals health."""

        self.hp += healing

        pass


###########################################################################################
# Interface for testing current program
###########################################################################################
###########################################################################################
###########################################################################################

shakila = Pokemon()

shakila.createpokemon()

print(shakila)

while shakila.hp > 0:
    damage = int(input("How hard do you want to hit Shakila?"))

    shakila.takedamage(damage)

    print(shakila)

print("Congrats! You knocked out Shakila!")

while shakila.hp < 1:

    healing = int(input("How hard do you want to heal Shakila?"))

    shakila.gainhealth(healing)

    print(shakila)

print("Boo. You saved Shakila.")