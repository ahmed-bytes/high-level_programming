from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
mm = MoneyMachine()
m = Menu()

is_Off = False

while not is_Off:
    options = m.get_items()
    user_choice = input(f"What would you like? ({options}): ").lower()

    if user_choice == "off":
        is_Off = True
    elif user_choice == "report":
        cm.report()
        mm.report()
    else:
        drink = m.find_drink(user_choice)
        if cm.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
            cm.make_coffee(drink)
