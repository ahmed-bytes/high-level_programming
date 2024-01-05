"""Coffee Machine Simultation."""
import data as d
# Makes 3 hot flavors
# Expresso: 50ml, 18g $1.50   Latte: 200ml 24g 150ml $2.50  Cappuccino: 250ml 24g 100ml $3.00
# Coffee: Tank: 300ml, Milk: 200ml, Seed: 100g
# Coin_operated: Penny: 1, Nickel: 5, Dime: 10, Quarter: 25


def print_resource():
    """Print the resources in the machine"""
    water = d.resources["water"]
    milk = d.resources["milk"]
    coffee = d.resources["coffee"]

    print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nProfit: ${PROFIT}")


def resource_sufficient(ingredients):
    """Checks for enough resource in the ingredient."""
    for items in ingredients:
        if ingredients[items] > d.resources[items]:
            print(f"There's no enough {items}")
            return False
    return True


def process_coins():
    """Calculate the User coin."""
    print("Please Enter Coins")
    total = int(input("How many Quarters?: ")) * 0.25
    total += int(input("How many Dimes?: ")) * 0.10
    total += int(input("How many Nickels?: ")) * 0.05
    total += int(input("How many Pennies?: ")) * 0.01
    return total


IS_ON = True
PROFIT = 0

while IS_ON:
    user_prompt = input(
        "What would you like? (espresso/latte/cappuccino) ").lower()

    if 'report' in user_prompt:
        print_resource()
    elif 'off' in user_prompt:
        IS_ON = False
    else:
        drink = d.MENU[user_prompt]
        if resource_sufficient(drink["ingredients"]):
            payment = process_coins()

            if payment < drink["cost"]:
                print("Sorry, Not Enough Money :( . Money Refunded!!! ")
            else:
                if payment > drink["cost"]:
                    PROFIT += drink["cost"]
                    change = round(payment - drink["cost"], 2)
                    print(f"Here's your change: ${change}")
