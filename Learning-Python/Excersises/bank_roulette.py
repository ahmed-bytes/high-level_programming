#!/usr/bin/python3
from random import choice

names = input("Enter Names seperated by comma: ")
name_list = names.split(", ")
print("{} is paying for everybody :)".format(choice(name_list)))
