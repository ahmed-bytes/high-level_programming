import data as people
from ascii_art import HIGHER_LOWER_LOGO
from random import choice

print(HIGHER_LOWER_LOGO)
game_over = 'no'

while not game_over:
    compare_a = choice(people.data)
    compare_b = choice(people.data)
    print(
        "Compare A: {compare_a[name]}, a {compare_b[description]}, from {['country']}.")
