from manu import MENU , resources

profite = 0
should_make_coffee = True

def process_coin():
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dime? ")) * 0.10
    total += int(input("How many nickle? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    print(f"Total amount is ${round(total,2)}")
    return total

def check_resources(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry there is not enough {items}")
            return False
    return True

def make_coffee(choice,update_ingredients):
    for items in update_ingredients:
        resources[items] -= update_ingredients[items]

    print(f"Here is your {choice}☕ . Enjoy")


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"water: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}g\nmoney: {profite}$")

while should_make_coffee:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        report()
    elif choice == "off":
        break
    else:
        drink = MENU[choice]
        have_resources = check_resources(drink["ingredients"])
        if have_resources:
            amount = process_coin()
            drink_cost = drink["cost"]
            if amount >= drink_cost:
                change =round(amount-drink_cost,2)
                print(f"Here is your ${change} dollars in change.")
                profite += drink_cost
                make_coffee(choice, drink["ingredients"])
            else:
                print("Sorry that's not enough money. Money refunded.")

