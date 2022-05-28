##
 # -----------------------------------------------------------------------------
 # Created by Ulysses Carlos on 06/02/2020 at 08:23 PM
 # 
 # Example04.py
 # 
 # -----------------------------------------------------------------------------
 ##
 
cars = 100
car_space = 4
drivers = 30
passengers = 90

cars_not_driven = (cars - drivers)
cars_driven = drivers

carpool_capacity = cars_driven * car_space
average_car_passengers = (passengers / cars_driven)

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_car_passengers, "in each car.")
