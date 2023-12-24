#!/usr/bin/python3
from random import choice

if __name__ == "__main__":
    names = input("Enter Names seperated by comma: ")
    name_list = names.split(", ")
    print("{} is paying for everybody :)".format(choice(name_list)))
