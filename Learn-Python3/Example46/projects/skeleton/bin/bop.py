#!/usr/bin/env python3
from time import sleep


def print_picture():
    with open("ranfa.txt") as file:
        print(file.read())


def bopper():
    print("The only purpose of this program is to "
          + "test out the project hierarchy introduced in "
          + "Example 46. Yep. Here's a picture for your troubles."
          )
    sleep(1)
    print_picture()


# Run
bopper()
