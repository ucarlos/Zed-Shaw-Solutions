# -----------------------------------------------------------------------------
# Created by Ulysses Carlos on 06/17/2020 at 03:05 PM
# 
# Example43.py
# My code for Example 43.
# -----------------------------------------------------------------------------

# Global variables?
prompt_character = "> "
seen_opening = False

class Scene(object):
    def enter(self):
        pass


class Engine(object):
    def __init__(self, scene_map):
        pass

    def play(self):
        pass


class Death(Scene):
    def enter(self):
        pass


class CentralCorridor(Scene):

    def unique_enter(self):
        print("Your normal day on the USS Andromeda is suddenly interrupted" +
              "by the sound of alarms going off. Then, a bright flash of light knocks you" +
              "conscious. When you come to, you find yourself in the Central Corridor" +
              ", but you can make the faint sound of some... high pitched monster?" +
              "You've heard this before and recognize that the sound belongs" +
              "to Gothons, one of the most obnoxious species in the galaxy." +
              "You have to do something, but what?")

        print("\"You encounter a Gothon by the way\"" +
              ", says your inner voice. \"What do?\"")
        action = input(prompt_character)

        # Actions:
        # Tell a joke
        # Run away
        # Attack
        # help
        # Lowercase
        action.lower()

        # Do a loop
        while True:
            if action == "help":
                print("You hear your inner voice...")
                print("\"Alright, so you got these options.\"")
                print("Tell joke - tells a joke to the Gothon. Duh.")
                print("Run away - You run away. Duh.")
                print("Attack - You attack the Gothon. Duh.")
                print("These are all the options the developer allows you to do.")
                print("I won't accept any other option. Sorry, we're on a budget!")

            elif action == "tell joke":
                print("You attempt to tell a joke to the Gothon.")
                print("Your awful joke touches the Gothon to the core" +
                      "and he suddenly catches on fire.")
                print("His final words are \"God, that's one awful joke..\"")
                print("But whatever, he's gone. Time to go on!")
                break

            elif action == "attack":
                print("You ready your laser pistol and fire at the Gothon" +
                      ", but nothing happens.")
                print("You forget that the central corridor has an " +
                      "anti-laser field that prevents any laser-based"
                      + " weapon from firing.")
                print("The Gothon takes advantage of this situation"
                      + " by killing you.")
            elif action == "run away" or action == "run":
                print("You try to run away, but fail! The Gothon catches up"
                      + "to you and eats you.")
        # Take action somehow:

        # Now, you move on:
        return "central_corridor"

    def enter(self):
        if not seen_opening:
            unique_enter()

        # Just display the
        print("For whatever reason, you're back in the central corridor." +
              "What do you do?")

        # If you return, then just take a nap, head back,
        while True:
            action = input(prompt_character)
            action.lower()

            if action == "help me" or "help" or "h":
                print("You hear a voice in your head...")
                print("The only options you have at this point is to \"head" +
                      "back\" or \"take a nap\". In my opinion, you should take" +
                      " the second option.")
            elif action == "take a nap" or "nap":
                print("You decide to take a nap and awake to " +
                      "the sound of an explosion. Apparently, the Gothons " +
                      "decided to destroy the ship. You die in the aftermath.")
            elif action == "back" or "head back" or "go back":
                print("You decide to head back from where you came.")
                break
            else:
                print("You hear a voice in your head:")
                print("\"Sorry, that's not an available option. If you're lost " +
                      "Why not use the \"help\" option?")

            # Implement a go-back option
            # Stop


class LaserWeaponArmory(Scene):
    # option to give initial and returning options.
    # Will be shared amongP all objects.
    def initial_enter(self):
        print("You find yourself in the Laser Weapon Armory."

    def enter(self):
        if first_time_in_room:
            return initial_enter()
        else:
            # Do default options


class TheBridge(Scene):
    def enter(self):
              pass


class EscapePod(Scene):
    def enter(self):
        pass


class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):




def initialize_rooms():
    # First, make sure that list is empty:
    list = []
    # Next, make sure that you have the following rooms:
    return list


# End of Classes:
a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
