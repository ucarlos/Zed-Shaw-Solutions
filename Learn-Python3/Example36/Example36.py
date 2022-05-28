##
 # -----------------------------------------------------------------------------
 # Created by Ulysses Carlos on 06/06/2020 at 08:28 PM
 # 
 # Example36.py
 # This a text-based game in the vein of Example35.py. As always, ignore
 # the pep8 bitching about the indention. It's a banner.
 # -----------------------------------------------------------------------------
 #/

# Introduction_text
# import Music
from sys import exit
prompt_char = "> "


def check_valid_string(string, low, high):
    if not string.isnumeric():
        print("Wait, that's not right. Let's try again.")
        return False
    # Now take the number as int.
    num = int(string)
    if not (num in range(low, high)):
        print("You realize that you can't take that option and decide to try again.")
        return False
    else:
        return True


def game_over(reason):
    print(reason)
    exit(0)


def intro():
    print("""The sound of raindrops awakes you up from your sleep. Your first thoughts are
immediate fear. You're not in your bedroom. Instead, you in some form of room?
It's quite hard to see your surrondings. You instinctly reach for your light,
but your left hand finds nothing to grab onto. You look down and realize that
you've been sleeping on cold hard rock. You then look up and see the giant hole
in the ceiling, illuminated by moonlight. You vaguely see the number '1'
chiseled on the floor. After getting up, you try to search your pockets for
your pistol and cellphone, but instead you feel some crumbled up object. Using
the moonlight, you can faintly make out the words "Wumpus" and "escape".
Wumpus. Wumpus. You've heard that name before. After pondering for a moment
on the meaning of the word, you can faintly hear some form of roar from one
corner of the room. You slowly walk up and faintly see some number
displayed on a plaque above a hole. Suddenly, the room is illuminated.
You then notice that this hole is the only way out of this room. It's time
to get out of here.
""")


# Room 1:
def room1():
    print("""In front of you, a dark tunnel lies ahead.\n
A plaque on top of the entrance reads '2'. You have to make a decision. 
""")
    print("1) Go through the tunnel to some unknown destination.")
    print("2) Remain in this room")
    print("3) Sleep")

    result = (input(prompt_char))
    while True:
        if not result.isnumeric():
            print("Wait, that's not right. Let's try again.")
            result = int(input(prompt_char))
        elif int(result) not in range(1, 4):
            print("You realize that you can't take that option and decide to try again.")
            result = int(input(prompt_char))
        else:
            break

    if int(result) == 1:
        print("You decide to go through the tunnel.")
        room2()
    elif int(result) == 2:
        game_over("You decide to stay in the room indefinitely. You later die of starvation.")
    elif int(result) == 3:
        print("You decide to take a quick nap.")
        room1()


# Room 2:
def room2():
    print("""After stepping into the room, you are welcomed by the faint
    smell of rotten eggs. It's coming from one of the tunnels, which you see heading
    to the rooms 3 and 4. What do you do?""")
    print("1) Go to room 3")
    print("2) Go to room 4")
    print("3) Go back to room 1.")
    print("4) Take a quick rest")
    
    result = input(prompt_char)
    # Check for valid input and in range 0, 3. 
    while True:
        bool = check_valid_string(result, 1, 5)
        if bool:
            break
        else:
            result = input(prompt_char)

    # Now make the decision:
    num = int(result)
    # There really should be switches holy shit
    if num == 1:
        print("You decide to head over to room 3.")
        room3()
    elif num == 2:
        print("You decide to head over to room 4.")
        room4()
    elif num == 3:
        print("You decide to head back to room 1.")
        room1()
    else:
        print("You take a quick break and rest on the floor.")
        room2()

# Room 3:


def room3():
    print("""You step in the room and your nostrils are immediately attacked
by the awful stench of death and garbage. Out of the corner of your eyes, you see
something moving that grabs your attention. It's a wumpus! Unable to stand the smell, you quickly run back to the tunnel, but the wumpus attacks you and you die.""")
    game_over("")


# Room 4:
def room4():
    print("""Your nostrils thank you for entering this room. On your left you see a tunnel to room 6 and on your left you see a tunnel to room 5. You hear a faint wind coming from one of tunnels, but you can't make out anything else. What do you do now?""")
    print("1) Go to room 5")
    print("2) Go to room 6")
    print("3) Go back to room 2")
    print("4) Take a quick nap.")
    result = input(prompt_char)
    
    while True:
        bool = check_valid_string(result, 1, 5)
        if bool:
            break
        else:
            result = input(prompt_char)
        
    # Now make the choice:
    num = int(result)
    if num == 1:
        print("You decide to go to room 5.")
        room5()
    elif num == 2:
        print("You decide to go to room 6.")
        room6()
    elif num == 3:
        print("You decide to head back to room 2.")
        room2()
    else:
        print("You notice a bedroll on the floor and decide to sleep for a little bit.")
        room4()


def room5():
    print("After walking for what seems to be an eternity, you finally reach the end of tunnel. You're out of the dungeon, and realize that you're not that far from your home. You arrive home and decide to take a long rest in your bedroom.")
    game_over("You win I guess.")


# Room 6:
def room6():
    game_over("The sound of wind grows louder and louder as you reach the end of the tunnel. Suddenly, you trip and fall into a pit. After several minutes, you reach terminal velocity and die as your body impacts the ground.")


# Main function
def main():
    # play_room1()
    intro()
    room1()


# Run the game.
main()
