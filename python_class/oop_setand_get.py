#!/usr/bin/python3
# File name

class robot:
    def __init__(self, name = None, b_year = None):
        self.name = name
        self.b_year = b_year

    def say_hi(self):
        if self.name:
            print("Hi, my name is" + self.name)
        else:
            print("Hi, I have no name")
        if self.b_year:
            print("I was built in {:d}".format(self.b_year))
        else:
            print("I was never created, i exist with time")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_b_year(self, b_year):
        self.b_year = b_year

    def get_b_year(self):
        return self.b_year

Rb1 = robot("Alpha1", 2900)
Rb2 = robot()
Rb2.set_name("Beta-B1")
Rb1.say_hi()
Rb2.say_hi()
print(Rb1.get_name())
print(Rb2.get_name())
print(Rb1.get_b_year())
print(Rb2.get_b_year())
Rb2.set_b_year(3000)
print(Rb2.get_b_year())
