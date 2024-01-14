from prettytable import PrettyTable
from random import randint

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirrel", "Charmander"], "c")
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)


# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cats = Cat("Garfield", randint(0,100))
cats2 = Cat("Ginger", randint(0,100))
cats3 = Cat("Puss", randint(0,100))

def oldest(*args):
    """
    @*args: int
    @rtype: int
    """
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldest(cats.age, cats2.age, cats3.age)} years old")
