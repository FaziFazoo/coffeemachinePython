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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


is_on = True


def report(resource):
    """Print report of resources"""
    print(f"Water : {resource['water']}ml")
    print(f"Milk  : {resource['milk']}ml")
    print(f"Coffee: {resource['coffee']}g")
    print(f"Money : {profit}")


def is_resource_sufficient(resource, needed_resource):
    """return true if resource is sufficient else return false"""
    for item in resource:
        if resource[item] >= needed_resource[item]:
            return True
        else:
            print(f"Sorry there is not enough {item}.")
            return False


def process_coins():
    """Function to process coins"""
    print("Please insert coins.")
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: "))*0.10
    total += int(input("how many nickles?: "))*0.05
    total += int(input("how many cents?: "))*0.01
    return total


def is_transaction_success(total_money, needed_money):
    """Return true if user gave more money than needed money else return false"""
    if total_money < needed_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(total_money-needed_money, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += needed_money
        return True


def make_coffee(resource, needed_resource, drink_name):
    for item in needed_resource:
        resource[item] -= needed_resource[item]
    print(f"Here is your {drink_name}☕. Enjoy!")


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        report(resources)
    else:
        drink = MENU[choice]
        if is_resource_sufficient(resources, drink['ingredients']):
            payment = process_coins()
            if is_transaction_success(payment, drink['cost']):
                make_coffee(resources, drink['ingredients'], choice)
