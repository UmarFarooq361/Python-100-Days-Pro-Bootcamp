from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
# menu_item = MenuItem()




should_make_coffee = True

while should_make_coffee:
    options = menu.get_items()
    choice = input(f"What would you like? {options}")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        break
    else:
        drink = menu.find_drink(choice)
        have_resources = coffee_maker.is_resource_sufficient(drink)
        if have_resources:
            if  money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


