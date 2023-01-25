from Beginner_training import *


animal1 = pets(pet_name="godzilla", species="kaiju", domesticated=True, extinct=False)
print(animal1.hold())

person1 = person(name="francis", occupation="write none sense code")
print(person1.hold())

robot1 = generate()
print(robot1.hold())
print("robot1 version: ",robot1.mecha_version)
print("updgrade robot1 version:", robot1.upgrade())
print("updgrade robot1 version:", robot1.upgrade())
print("updgrade robot1 version:", robot1.upgrade())
print("updgrade robot1 version:", robot1.upgrade())
print(f"robot1 Generating lottery numbers: {robot1.gen_numbers()}")
user_age = int(input("Enter your age:"))
print(f"robot1 will use machine learning to predict your birth year 90% accurate: {robot1.predict_year(user_age)}")
print("pythagorean:")
side1 = int(input("Enter Side A:"))
side2 = int(input("Enter Side B:"))
print(f"pythagorean: Side C: {robot1.pythagorean(sideA=side1, sideB=side2)}")
print("END")


if __name__ == "__main__":
    main()