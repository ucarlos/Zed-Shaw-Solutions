ten_things = "Apples Oranges Crows Telephone Light Sugar"
print(f"{ten_things}")
print("Wait, there are not 10 things in that list. Let's fix that.")

# split(ten_things, " ")
stuff = ten_things.split(" ")

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # pop(more_stuff)
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # append(stuff, next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
# Shouldn't this just bring the last item?
print(stuff[-1]) # Whoa! Fancy!
# pop(stuff)
print(stuff.pop())

# Uses whatever is joined as separator.
# join(stuff, " ")
print(" ".join(stuff)) # ??
# This should be items 3,4, and maybe 5?

# join(stuff[3:5], "#"
print("#".join(stuff[3:5]))
