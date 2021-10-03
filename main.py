from menu import MENU, resources

is_continue = True
espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]
money = 0


# TODO: If the transaction is successful and there are enough resources to make the drink the
#   user selected, then the ingredients to make the drink should be deducted from the
#   coffee machine resources.

def check_remaining_product(coffee_type):
    require = MENU[coffee_type]["ingredients"]
    for item in require:
        if require[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def is_resources_sufficient(coffee_type):
    new_water = MENU[coffee_type]["ingredients"]["water"]
    new_coffee = MENU[coffee_type]["ingredients"]["coffee"]
    if coffee_type == "espresso":
        resources['water'] -= new_water
        resources['coffee'] -= new_coffee
    else:
        new_milk = MENU[coffee_type]["ingredients"]["milk"]
        resources['water'] -= new_water
        resources['milk'] -= new_milk
        resources['coffee'] -= new_coffee


# TODO: Calculate the monetary value of the coins inserted.
def money_calculator(coffee_type):
    coffee_price = MENU[coffee_type]["cost"]
    print("Please insert coins.")
    quarter = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.1
    nickles = int(input("How many nickles: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.1
    total = quarter + dimes + nickles + pennies
    changes = round(total - coffee_price, 2)

    # TODO: Check that the user has inserted enough money to purchase the drink they selected.
    if total < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
    else:
        # TODO: If the user has inserted too much money, the machine should offer change.
        print(f"Here is ${changes} in change.")
        # TODO: Once all resources have been deducted
        print(f"Here is your {coffee_type} ☕️. Enjoy!")
        # TODO: But if the user has inserted enough money, then the cost of the drink gets added to the
        #    machine as the profit and this will be reflected the next time “report” is triggered.
        global money
        money += coffee_price
        is_resources_sufficient(coffee_type)


# TODO: The prompt should show every time action has completed, e.g. once the drink is dispensed.
while is_continue:

    # TODO: Check the user’s input to decide what to do next.
    print("")
    coffee_type = input(
        f"What would you like? (espresso ${espresso_price}/latte ${latte_price}/cappuccino ${cappuccino_price}): ")

    # TODO: Turn off the Coffee Machine by entering “ off ” to the prompt.
    if coffee_type == "off":
        is_continue = False
    # TODO: When the user enters “report” to the prompt, a report should be generated that shows the current resource
    #  values.
    elif coffee_type == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        # TODO: If there are sufficient resources to make the drink selected, then the program should
        #    prompt the user to insert coins.
        if check_remaining_product(coffee_type):
            money_calculator(coffee_type)
