#!/usr/bin/python3
from random import randint

prompt = input("Heads or Tails: ").upper()
if randint(0, 1) == 0:
    print("Heads")
    if prompt == "HEADS":
        print("You Won!!")
    else:
        print("You lost!! ")
else:
    print("Tails")
    if prompt == "TAILS":
        print("You Won!!")
    else:
        print("You lost!! ")
