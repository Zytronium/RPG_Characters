#!/usr/bin/python3


class Character:
    def __init__(self, name="", stats=[], abilities=[], inventory=[], position=[0, 0]):
        self.name = name
        self.stats = stats
        self.abilities = abilities
        self.inventory = inventory
        self.position = position

    def __repr__(self, char_type="Character"):
        return f"{char_type}(\"{self.name}\", {self.stats}, {self.abilities}, {self.inventory}, {self.position})"

    def move(self, x, y):
        self.position[0] += x
        self.position[1] += y
        print("position: {}".format(self.position))


class Hero(Character):
    def __init__(self, name="", stats=[], abilities=[], inventory=[], position=[0, 0], allegiance=""):
        super().__init__(name, stats, abilities, inventory, position)
        self.allegiance = allegiance

    def __repr__(self, char_type="Hero"):
        super().__repr__(self, char_type)

    def input(self, key=""):
        match key:
            case "w":
                self.move(1, 0)
            case "s":
                self.move(-1, 0)
            case "a":
                self.move(0, -1)
            case "d":
                self.move(0, 1)


class Villain(Character):
    pass

string = "hello world"
list = [1, 2, "five"]
person = Hero()
print(string)
print(repr(string))
print(list)
print(repr(list))
print(person)
print(repr(person))

print(person)
while True:
    person.input(input())

