"""Calculate the amount of can reqquired to paint a wall."""
from math import ceil


def paint_calc(height, width, cover):
    """
    paint_calc: Amount of cans needed.

    height: int height of the wall,
    width: int width of the wall,
    cover: int total meters of the wall.
    """
    number_of_cans = ceil((height * width) / cover)
    return number_of_cans


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
result = paint_calc(height=test_h, width=test_w, cover=coverage)
print("You'll need {} cans".format(result))
