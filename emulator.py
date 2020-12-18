#####################
# Raymond and Ashton's Pokemon Emulator
#####################

class Pokemon:
    """Pokemon class"""
    def __init__(self, name="None", t="None", level=0):
        """Override of initialization for the Pokemon
        *Needs to be updated when new variables are added*

        Current variables attached to Pokemon:
        Name (str)
        Type (str)
        Level (int)

        """
        self.name = name
        self.type = t
        self.level = level

    def __repr__(self):
        """Override of print function for Pokemon class
        *Needs to be updated when new variables are added*
        """
        return "Level " + str(self.level) + " " + self.name + ". " + self.type + " type."

    def createpokemon(self):
        """Function called creating Pokemon
        *Needs to be updated when new variables are added*

        Current variables attached to Pokemon:
        Name (str)
        Type (str)
        Level (int)
        """
        name = input("What is the pokemons name?").strip().lower()
        t = input("What is " + name + "'s type?").strip().lower()
        check = True
        while check:
            # this system ensures pokemon level is a valid number (1-100)
            # will loop through until valid number is entered

            level = input("What is " + name + "'s level?").strip()

            try: # tests for if input was an integer, if so, executes code.
                level = int(level)

                if level <= 0: # test case for if input was equal to or below 0
                    print("Levels are a whole number from 1-100. It cannot be below 1. Please try again.")

                elif level > 100: # test case for if input was above 100
                    print("Levels are a whole number from 1-100. It cannot be above 100. Please try again.")

                else: # leaves loop if input is whole number from 1-100
                    check = False

            except ValueError: # if value is not an integer, prints this message
                print("Level has to be a whole number from 1-100. Please try again.")

        self.name = name
        self.type = t
        self.level = level

        pass

###########################################################################################
# Interface for testing current program
###########################################################################################
###########################################################################################
###########################################################################################


ashton = Pokemon()

ashton.createpokemon()

print(ashton)