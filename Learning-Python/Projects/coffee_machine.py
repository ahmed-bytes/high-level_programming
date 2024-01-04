"""Coffee Machine Simultation."""
# Makes 3 hot flavors
# Expresso: 50ml, 18g $1.50   Latte: 200ml 24g 150ml $2.50  Cappuccino: 250ml 24g 100ml $3.00
# Coffee: Tank: 300ml, Milk: 200ml, Seed: 100g
# Coin_operated: Penny: 1, Nickel: 5, Dime: 10, Quarter: 25


def report():
    """The Resources in The Coffee Machine."""
    water = 300
    milk = 200
    seed = 100
    money = 0
    print(f"Water: {water}ml\nMilk: {milk}ml\nSeed: {seed}\nMoney: {money}\n")


def calc_espresso(p, n, d, q):
    penny = 0.01 * p
    nickel = 0.05 * n
    dime = 0.10 * d
    quarter = 0.25 * q


user_prompt = input(
    "What would you like? (espresso/latte/cappuccino) ").lower()

if 'report' in user_prompt:
    report()

if 'espresso' or 'latte' or 'cappuccino' in user_prompt:
    user_penny = input("How many Penny: ")
    user_nickel = input("How many Nickel: ")
    user_dime = input("How many Dime: ")
    user_quarter = input("How many quarter: ")

    if 'espresso' in user_prompt:
        calc_espresso(user_penny, user_nickel, user_dime, user_quarter)
