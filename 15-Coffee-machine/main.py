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


def check_resource(item):
    for i in resources:
        if resources[i] < item[i]:
            return False
        return True


def show_report():
    for i in resources:
        print(f"{i} : {resources[i]}")


def payment(q, d, n, p):
    return 0.25 * q + 0.10 * d + 0.05 * n + 0.01 * p


def money_to_return(menu_, money):
    if money < menu_:
        print("Not enough dear")
        return False
    else:
        returned = money - menu_
        print(f"Here is your change: {round(returned, 2)}")
    return True


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


end_check = False
while not end_check:
    menu = input("What do you want to buy (Espresso, Latte, Cappuccino)?  ").lower()
    if menu == "report":
        show_report()
    else:
        drink = MENU[menu]

        if check_resource(drink["ingredients"]):
            print("Please insert Coins: ")
            quarters = int(input("How many Quarters? "))
            dimes = int(input("How many Dimes? "))
            nickles = int(input("How many Nickles? "))
            pennies = int(input("How many Pennies? "))
            money_taken = payment(quarters, dimes, nickles, pennies)
            if money_to_return(drink["cost"], money_taken):
                make_coffee(menu, drink["ingredients"])

    dec = input("Want another one? Y or N").lower()
    if dec == "no":
        end_check = True
