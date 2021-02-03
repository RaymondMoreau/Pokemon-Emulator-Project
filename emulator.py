#####################
# Raymond and Ashton's Pokemon Emulator
#####################

import random

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
        name = input("What is the pokemons name? ").strip().lower().capitalize()

        t = input("What is " + name + "'s type? ").strip().lower().capitalize()

        check = True
        while check:
            # this system ensures pokemon level is a valid number (1-100)
            # will loop through until valid number is entered

            level = input("What is " + name + "'s level? ").strip()

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

            health = input("What is " + name + "'s health? ").strip()

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

input("Welcome to the world of Pokemon! Let's get started by creating your pokemon. Press Enter to continue.\n")

poke = Pokemon()

poke.createpokemon()

print("\nCongratulations! You have created your own Pokemon! Here's what it looks like:")

print(poke)

input("Press enter to continue.\n")

print("We will now fight a training dummy. Use your moves to take it down before it beats you!")

dummy = Pokemon("Dummy", "Dummy", 5, 20)

print("Here's the dummies stats: " + str(dummy))

input("Press Enter to continue into the fight!\n")

charge = 0

while dummy.hp > 0: # battles until dummy is 'dead'

    print("Here's how much health the dummy has left: " + str(dummy.hp))

    print("And " + poke.name + " has " + poke.hp + " left!\n")

    charge = charge + 1

    print("Let's attack the dummy! Here are your moves:")

    print("(1) Light attack: 5 damage")

    print("(2) Strong attack: 10 damage (" + str(charge) + "/3 charges, generates one charge per turn)\n")

    answer = int(input("Type 1 or 2 to choose which attack to use! (Can't choose strong attack unless charged)\n").strip())

    check = True

    while check: # ensures input was a valid attack
        if type(answer) != int:

            print("That is not an number. Type in 1 or 2 to use a move!")

            answer = input("Type 1 or 2 to choose which attack to use! (Can't choose strong attack unless charged)\n").strip()

        elif answer > 2:

            print("That is not 1 or 2. Type in 1 or 2 to use a move!")

            answer = input("Type 1 or 2 to choose which attack to use! (Can't choose strong attack unless charged)\n").strip()

        elif answer < 1:

            print("That is not 1 or 2. Type in 1 or 2 to use a move!")

            answer = input("Type 1 or 2 to choose which attack to use! (Can't choose strong attack unless charged)\n").strip()

        elif answer == 2 and charge < 3:

            print("You cannot use the Strong attack (2) because it is not charged!")

            answer = input("Type 1 or 2 to choose which attack to use! (Can't choose strong attack unless charged)\n").strip()

        else:
            check = False

    # pokemon doing damage phase

    if answer == 1:

        print("You chose the light attack! Get him, " + poke.name + "!")

        print(poke.name + " did 5 damage to the dummy!")

        dummy.takedamage(5)

    if answer == 2:

        print("You chose the heavy attack! Hit him hard, " + poke.name + "!")

        print(poke.name + " did 10 damage to the dummy!")

        dummy.takedamage(10)

    # dummy doing damage phase

    if dummy.hp > 0:

        input("Good job, " + poke.name + "! Uh-oh, it looks like the dummy is fighting back! Press Enter to continue.\n")

        dummydam = random.randint(1, 10)

        print("The dummy hit " + poke.name + "! It did " + str(dummydam) + " damage!")

        poke.takedamage(dummydam)

    if poke.hp < 0:

        print("Oh no! " + str(poke.hp) + " fainted! We lost the battle!")

        dummy.hp = 0

        print("Better luck next time!")

    if dummy.hp < 0:

        print("you did it good job die")