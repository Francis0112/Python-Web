

# day 6
# OOP Exercise

# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle():
    def __init__(self, maxspeed,mileage) -> None:
        self.maxspeed=maxspeed
        self.mileage=mileage
# mars_rover = Vehicle(52,52320)
# print("Mars Rover: ",mars_rover.maxspeed, mars_rover.mileage)


# OOP Exercise 2: Create a Vehicle class without any variables and methods
class Vehicle():
    pass

# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle():
    def __init__(self, name, speed, mileage) -> None:
        self.name=name
        self.speed=speed
        self.mileage=mileage
class Bus(Vehicle):
    pass
# bus1 = Bus("Bus A", 250,32540)
# print(f"Bus name: {bus1.name} speed: {bus1.speed} mileage: {bus1.mileage}")

# OOP Exercise 4: Class Inheritance
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
class Vehicle():
    def __init__(self, name, speed, mileage) -> None:
        self.name=name
        self.speed=speed
        self.mileage=mileage

    def seating_capacity(self, capacity=50):
        return f"seating capacity of this {self.name} is {capacity}"

class Bus(Vehicle):
    pass
# bus2 = Bus("Bus B",300,1000)
# print(bus2.name,bus2.speed,bus2.mileage,bus2.seating_capacity())

# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
class Vehicle():
    color="white"
    def __init__(self,name,speed,mileage) -> None:
        self.name=name
        self.speed=speed
        self.mileage=mileage
class car(Vehicle):
    pass
class boat(Vehicle):
    pass
# a = car("tesla", 1200, 6200)
# b = boat("titanic", 130, 72120)
# print(a.color, a.name)
# print(b.color, b.name)


# OOP Exercise 6: Class Inheritance
# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

class Vehicle():
    
    def __init__(self, name, speed, mileage, capacity) -> None:
        self.name=name
        self.speed=speed
        self.mileage=mileage
        self.capacity=capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    
    def fare(self):
        amt = super().fare()
        mainte = amt*0.1
        total = amt+mainte
        return total
        
bus1 = Bus("bus A", 120, 650120, 20)
print(bus1.name, bus1.capacity, bus1.fare())


# OOP Exercise 7: Check type of an object

print(type(bus1))


# OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class

print(isinstance(bus1, Vehicle))
