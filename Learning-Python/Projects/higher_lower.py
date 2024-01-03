"""Simultaion of the game HigherLower."""
import random
import os
import data as people
from ascii_art import HIGHER_LOWER_LOGO, HIGHER_LOWER_VS


def format_data(account):
    """Sort the dict in the list."""
    acct_name = account['name']
    acct_desc = account['description']
    acct_from = account['country']
    return f"{acct_name}, a {acct_desc} from {acct_from}"


def compare(accounta, accountb):
    """Compare the highest num in a dict."""
    if accounta['follower_count'] > accountb['follower_count']:
        return 'A'
    return 'B'


print(f'\t\t{HIGHER_LOWER_LOGO}\n\n')
SCORE = 0
GAME_OVER = False
compare_a = random.choice(people.data)

while not GAME_OVER:
    compare_b = random.choice(people.data)
    initial_a = compare_a
    if compare_a == compare_b:
        compare_b = random.choice(people.data)
    if compare_b['follower_count'] > compare_a['follower_count']:
        compare_a = compare_b

    print(f"Compare A: {format_data(initial_a)}.\n")
    print(HIGHER_LOWER_VS)
    print(f"Compare B: {format_data(compare_b)}\n\n")

    guess = input("Who has more followers (Type 'A' or 'B'): ").upper()

    if compare(initial_a, compare_b) == guess:
        SCORE += 1
        os.system("clear")
        print(HIGHER_LOWER_LOGO)
        print(f"You're Right, Your score is {SCORE}\n")
    else:
        print(f"You're Wrong, Your Final Score is {SCORE}\n")
        GAME_OVER = True
