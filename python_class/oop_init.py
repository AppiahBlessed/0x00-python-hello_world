#!/usr/bin/python3
# oop_init.py

class person:
    def __init__(self, name):
        self.name = name


    def SayHi(self):
        print("Hello, my name is", self.name)

bot = 'John'
p = person(bot)
p.SayHi()
