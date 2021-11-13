from coffee_logo import coffee_logo


def print_offer():
    '''Prints the available products in the machine'''

    choice = input(f" What would you like? (espresso/latte/cappuccino): ")
    return choice


def check_resources(resources_needed):
    '''Checks available resources in the machine'''

    global resources
    for item_available, quantity_available in resources.items():
        for item_needed, quantity_needed in resources_needed.items():
            if item_available == item_needed:
                if quantity_available > quantity_needed:
                    continue
                else:
                    print(f"There is not enought {item_needed}.")
                    return False
    return True


def process_coins(money_needed):
    '''Processes the transaction'''

    total_value_inserted = 0

    total_coins_inserted = {
                'quarters' : (0.25 * int(input('How many Quarters?: '))),
                'dimes' : 0.1 * int(input('How many Dimes?: ')),
                'nickels' : 0.05 * int(input('How many Nickelbacks?: ')),
                'pennies' : 0.01 * int(input('How many Pennies?: '))
    }

    for coin, value in total_coins_inserted.items():
        total_value_inserted += value

    if total_value_inserted > money_needed:
        print("Here's", "%.2f" %float(total_value_inserted - money_needed), "in change" )
        return True
    elif total_value_inserted == money_needed:
        return True
    else:
        print("Sorry that's not enough money. Money refunded")


def make_coffe(choice, resources_needed):
    '''Makes the coffe'''

    global resources

    for item_available, quantity_available in resources.items():
        for item_needed, quantity_needed in resources_needed.items():
            if item_available == item_needed:
                if quantity_available > quantity_needed:
                    resources[item_available] -= quantity_needed
                else:
                    print(f"There is not enought {item_needed}.")
                    return False
    return True
    print(f"Here's your {choice}, enjoy!")

def refill():
    '''Refills resources in the machine.'''

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    return resources


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_on = True

while machine_on == True:
    print(coffee_logo)
    choice = print_offer()

    if choice.lower() == 'report': #PRINTS AVAILBALE RECOURCES IN THE MACHINE
        print(resources)
        continue
    elif choice == "off":   #TURNS OFF THE COFFEE MACHINE
        machine_on = False

    elif choice in MENU.keys(): #CHECKS IF THE CHOICE IS BETTWEN THE AVAILABLE PRODUCTS
        if check_resources(MENU[choice]['ingredients']) == True: #CHECKS IF THERE ARE ENOUGH RECOURCES TO PREPARE THE PRODUCT
            if process_coins(MENU[choice]['cost']) == True: #CHECKS IF ENOUGH MONEY IS INSERTED
                make_coffe(choice, MENU[choice]['ingredients'])  #MAKES COFFEE
            else:
                print(f"{choice.title()} costs {MENU[choice]['cost']}.")
            continue
        else:
            continue

    elif choice.lower() == 'refill': #REFILLS THE RESOURCES IN THE MACHINE
        resources = refill()

    else:
        print("We don't have this choice at this moment.")

