#!/usr/bin/python3
# oop_objvar.py

class robot:
    population = 0
    
    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))

        robot.population += 1

    def die(self):
        print("{} is being destroyed".format(self.name))

        robot.population -= 1
        if robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are till {:d} robots alive".format(robot.population))

    def say_hi(self):
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        print("We have {:d} robots".format(cls.population))

# Create first robot
Rb1 = robot("Alpha-B1")
Rb1.say_hi()
Rb1.how_many()

# Create second robot
Rb2 = robot("Beta-B1")
Rb2.say_hi()
Rb2.how_many()

print("\nRobots can do some work here.\n")
print("Time to destroy these robots, HAHAHAHA!!!")

# Kill robots
Rb1.die()
Rb2.die()

robot.how_many()
