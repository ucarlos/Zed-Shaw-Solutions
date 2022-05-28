## Animal is an object (Yes, sort of confusing) look at the extra credit
class Animal(object):
    def __init__(self, vertebrate, age):
        self.is_veribate = vertebrate
        self.age = age


# A dog is a animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        super(Dog, self).__init__(True, age)
        self.name = name
        self.breed = breed

# A cat is an animal
class Cat(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.name = breed


# A person is an object
class Person(object):
    def __init__(self, age, sex, name):
        # ??
        self.name = name
        self.age = age
        self.sex = sex
        # Person has-a pet of some kind.
        self.pet = None


# A Employee is a person
class Employee(Person):
    def __init__(self, name, age, sex, salary):
        # What is this strange magic?
        # You invoke the constructor for the parent class.
        super(Employee, self).__init__(name, age, sex)
        self.salary = salary


# A fish is an object
class Fish(object):
    # All Fish have scales, live in water
    def __init__(self, boolean):
        self.has_scales = boolean


# A Salmon is a fish
class Salmon(Fish):
    def __init__(self, has_scales):
        super(Salmon, self).__init__(has_scales)


# A Halibut is a fish
class Halibut(Fish):
    def __init__(self, has_scales):
        super(Halibut, self).__init__(has_scales)


# Rover is a dog.
rover = Dog("Rover", 3, "Husky")

# Satan is a cat
satan = Cat("Satan", "Dogo")

# Mary is a person
mary = Person("Mary", "female", 20)

# Mary has a pet named Satan
mary.pet = satan

# Frank is an Employee
frank = Employee("Frank", "Male", 20, 120000)

# Frank has a pet named Rover
frank.pet = rover

# Flipper is a Fish
flipper = Fish(False)

# Crouse is a Salmon
crouse = Salmon(True)

# Harry is a Halibut.
harry = Halibut(True)
