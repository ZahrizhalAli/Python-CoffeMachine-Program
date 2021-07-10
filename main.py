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
profit = 0
is_on = True


def is_transaction_successfull(moneyreceived, cost):
    global profit
    if moneyreceived >= cost:
        change = round(moneyreceived - cost, 2)
        profit += cost
        print(f"Here is your ${change} of your change")
        return True
    else:
        print("Sorry you don't have enough money. Money Refunded")
        return False


def process_coins():
    total = int(input("how many quarters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.1
    total += int(input("how many nickles: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total


def make_coffee(drink_name, order):
    for item in order:
        resources[item] -= order[item]
    print(f"Here is your {drink_name}")


def is_resources_sufficient(drink_resource):
    for item in drink_resource:
        if drink_resource[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successfull(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])



