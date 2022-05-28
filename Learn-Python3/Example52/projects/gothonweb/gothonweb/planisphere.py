# ------------------------------------------------------------------------------
# Created by Ulysses Carlos on 07/28/2020 at 02:06 PM
#
# planisphere.py
#
# ------------------------------------------------------------------------------

from random import randint
from sys import exit
# Problems to Solve:
# You’ll notice that there are a couple of problems with our Room class
# and this map:

# We have to put the text that was in the if-else clauses that got printed
# before entering a room as part of each room. This means you can’t shuffle
# the planisphere around which would be nice. You’ll be fixing that up
# in this exercise.

# There are parts in the original game where we ran code that determined
# things like the bomb’s keypad code or the right pod. In this game we just
# pick some defaults and go with it, but later you’ll be given Study Drills
# to make this work again.

# I’ve just made a generic_death ending for all of the bad decisions,
# which you’ll have to  finish for me. You’ll need to go back through and add
# in all the original endings and make sure they work.

# I've got a new kind of transition labeled "*" that will be used for a
# 'catch-all' action in the engine.

# Class Descriptions

prompt_character = "> "

string_central_corridor = """
The Gothons of Planet Percal #25 have invaded your ship and destroyed your
entire crew. You are the last surviving member and your last mission is to
get the neutron destruct bomb from the Weapons Armory, put it in the bridge,
and blow the ship up after getting into an escape pod.

You're running down the central corridor to the Weapons Armory when a 
Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown
costume flowing around his hate-filled body. He's blocking the door
to the Armory and about the pull a weapon to blast you.
"""

string_cc_shoot = """
Quick on the draw, you yank out your blaster and fire
it at the Gothon. His clown costume is flowing and
moving around his body, which throws off your aim.
Your laser hits his costume but misses him entirely.
This completely ruins his brand new costume his mother
bought him, which makes him fly into an insane rage
and blast you repeatedly in the face until you are dead.
Then he eats you.
"""
string_cc_dodge = """
Like a world class boxer, you dodge, weave, slip, and slide right
as the Gothon's blaster cranks a laser past your head.
In the middle of your artful dodge, your foot slips and you bang
your head on the metal wall and pass out. You wake up shortly
after only to die as the Gothon stomps on your head and eats you. """

string_weapon_armory = """
Lucky for you, they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvgf
nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr. The Gothon stops, tries not
to laugh, then busts out laughing and can't move.
While he's laughing, you run up and shoot him square in the head putting him
down, then jump through the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan the room for more
Gothons that might be hiding. It's dead quiet, too quiet. You stand up and
run to the far side of the room and find the neutron bomb in its container.
There's a keypad lock on the box and you need the code to get the bomb out.
If you get the code wrong ten times, then the lock closes forever and you
can't get the bomb. The code is 3 digits.

"""
string_wa_fail = """
The lock buzzes one last time and then you hear a
sickening melting sound as the mechanism is fused
together. You decide to sit there, and finally the
Gothons blow up the ship from their ship and you die.
"""

string_the_bridge = """
The container clicks open and the seal breaks, letting gas out. You grab the
neutron bomb and run as fast as you can to the bridge where you must place it
in the right spot.

You burst onto the Bridge with the neutron destruct bomb under your arm and
surprise 5 Gothons who are trying to take control of the ship. Each of them
has an even uglier clown costume than the last. They haven't pulled their
weapons out yet, as they see the active bomb under your arm and don't want
to set it off.
"""
string_the_bridge_fail = """
In a panic, you throw the bomb at the group of Gothons
and make a leap for the door. Right as you drop it a
Gothon shoots you right in the back, killing you.
As you die, you see another Gothon frantically try to
disarm the bomb. You die knowing they will probably
blow up when it goes off.
"""

string_escape_pod = """
You point your blaster at the bomb under your arm and the Gothons put their
hands up and start to sweat. You inch backward to the door, open it, and then
carefully place the bomb on the floor, pointing your blaster at it.
You then jump back through the door, punch the close button and blast the lock
so the Gothons can't get out. Now that the bomb is placed, you run to the
escape pod to get off this tin can.

You rush through the ship deserately trying to make it to the escape pod before
the whole ship explodes. It seems like hardly any Gothons are on the ship, so
your run is clear of interference. You get to the chamber with the escape
pods, and now need to pick one to take Some of them could be damaged, but you
don't have time to look. There's 5 pods, which one do you take?
 """

string_end_success = """
You jump into Pod 2 and hit the eject button. The pod easily slides out into
space heading to the planet below. As it flies to the planet, you look
back and see your ship implode then explode like a bright star, taking
out the Gothon ship at the same time. You won!
 """

string_end_fail = """
You jump into a random pod and hit the eject button. The pod escapes out
into the void of space, then implodes as the hull ruptures, crushing your
body into jam jelly.
"""


class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.help = ""
        self.show_help = False

        # Determines how many times the player can be in the room.
        # Used for the bomb room.
        self.max_chances = -1

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
        self.create_help()

    def create_help(self):
        """
        Display all available options that can be taken.
        """
        if not self.paths:
            self.help = "This room is currently empty! Populate it!"
        else:
            self.help = "Here are the available options for this room:\n"

    def enable_help(self):
        self.show_help = True

    def disable_help(self):
        self.show_help = False

    def set_chances(self, value):
        """
        Set how many tries the player can be in the room
        before a game over occurs.
        """
        self.max_chances = value
        self.current_chances = value

    # def enter_room(self):
    #     # Enter the description and then place the options.
    #     print(self.description)
    #     user_input = input(prompt_character)
    #     user_input = user_input.lower()

    #     while not (user_input in self.path):
    #         print("You are chided by a voice in your head that you can't do"
    #               "that.")
    #         print("\"Please, choose a different option. The developer isn't "
    #               "capable")
    #         print("of writing an option like that. Try Again.\" ")

    #         user_input = input(prompt_character)

        # Now take the option:


class GenericDeath(Room):
    death_list = ["You died. You kinda suck at this.",
                  "Your mother would be proud... If she were smarter.",
                  "lol such a loser",
                  "I have a small puppy that's better than this.",
                  "You're worse than your Dad's jokes."]

    def __init__(self, description):
        super(GenericDeath, self).__init__("You died 💀", description)
        self.quip = self.death_list[randint(0, len(self.death_list) - 1)]
        pass

    def enter_room(self):
        print(self.description)
        exit(1)


central_corridor = Room("Central Corridor", string_central_corridor)
central_corridor_shoot = GenericDeath(string_cc_shoot)
central_corridor_dodge = GenericDeath(string_cc_dodge)

laser_weapon_armory = Room("Laser Weapon Armory", string_weapon_armory)
laser_weapon_armory.set_chances(10)
laser_weapon_armory_fail = GenericDeath(string_wa_fail)

the_bridge = Room("The Bridge", string_the_bridge)
the_bridge_fail = GenericDeath(string_the_bridge_fail)

escape_pod = Room("Escape Pod", string_escape_pod)
escape_pod.set_chances(1)
the_end_winner = Room("The End", string_end_success)

the_end_loser = Room("The End", string_end_fail)

# Escape Pod
escape_pod_random = randint(1, 5)
escape_pod.add_paths({str(escape_pod_random): the_end_winner,
                      '*': the_end_loser
                      })

the_bridge.add_paths({'throw the bomb': the_bridge_fail,
                      'slowly place the bomb': escape_pod})

random_code = randint(0, 9999)
laser_weapon_armory.add_paths({str(random_code): the_bridge,
                               '*': laser_weapon_armory_fail})

central_corridor.add_paths({'shoot!': central_corridor_shoot,
                            'dodge!': central_corridor_dodge,
                            'tell a joke': laser_weapon_armory
                            })

START = 'central_corridor'


class RoomContainer(object):
    def __init__(self, room_dict=None):
        # Set the default map
        if room_dict is None:
            self.map_list = {'central_corridor': central_corridor,
                             'cc_shoot': central_corridor_shoot,
                             'cc_dodge': central_corridor_dodge,
                             'laser_weapon_armory': laser_weapon_armory,
                             'lwa_fail': laser_weapon_armory_fail,
                             'the_bridge': the_bridge,
                             'the_bridge_fail': the_bridge_fail,
                             'escape_pod': escape_pod,
                             'the_end_winner': the_end_winner,
                             'generic_death': GenericDeath("YOU DIED"),
                             'the_end_loser': the_end_loser}
        else:
            self.map_list = room_dict

    def load_room(self, name):
        if name in self.map_list:
            return self.map_list[name]
        else:
            return None

    def append_to_list(self, key, value):
        self.map_list.update({key: value})

    def remove_from_list(self, key):
        self.map_list.pop(key)

    def name_room(self, room):
        for key in self.map_list:
            if self.map_list[key] == room:
                return key
        # Otherwise, return None if not found.
        return None
