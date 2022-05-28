def call_while(initial_val, length, increment_val):
    i = 0
    numbers = []

    while i < length:
        print(f"At the top i is {initial_val + i}.")
        numbers.append(initial_val + i)
        i += increment_val
        print("The list is now:", numbers)
        print(f"At the bottom i is {initial_val + i}")

    print("Now printing the entire list:")

    for i in numbers:
        print(i)


def main():
    result = int(input("How many numbers do you want? "))
    val = int(input("What is your initial value? "))
    increment_val = int(input("Increment by what value (default is 1) ? "))
    call_while(val, result, increment_val)


main()
