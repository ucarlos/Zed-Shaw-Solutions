# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# Ok, that *args is acutally pointless, we can just do this:
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


    
# This just takes on argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# This one takes no arguments
def print_none():
    print("I've got nothing.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
