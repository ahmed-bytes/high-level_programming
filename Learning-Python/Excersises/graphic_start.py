from turtle import Turtle
from random import choice

timmy = Turtle()

colours = ["red", "blue", "green", "pink", "wheat", "SlateGray"]
directions = [0,90,180,270]

timmy.shape("arrow")
timmy.color("red")
timmy.fillcolor("yellow")


def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


# for _ in range(10):
#     timmy.forward(90)
#     timmy.right(90)
#
# timmy.left(90)

timmy.pos()

# for _ in range(20):
#     timmy.pd()
#     timmy.forward(10)
#     timmy.pu()
#     timmy.forward(10)


for i in range(3, 11):
    timmy.color(choice(colours))
    draw_shapes(i)


