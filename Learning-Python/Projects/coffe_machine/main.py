from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_Off = False

while not is_Off:
    user_drink = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if user_drink == "off":
        is_Off = True
    elif user_drink == "report":
        CoffeeMaker.report()
    else:
        if CoffeeMaker.is_resource_sufficient(user_drink) == False:
            print("“Sorry there is not enough")