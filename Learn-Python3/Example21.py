def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b


def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b


print("Let's do some math with just functions:")
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print("")
print(f"Age: {age}  Height: {height}  Weight: {weight}")
print(f"IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.

print("Here's a puzzle:\n")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "\nCan you do it by hand?")
formula = age + (height - ((weight * iq) / 2))
print("Formula value: ", formula)
