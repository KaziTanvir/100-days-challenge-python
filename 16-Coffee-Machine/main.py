from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu= Menu()
end_check = True

while not end_check:
    order = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if order == "off":
        end_check = False
    elif order == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(order)
        sufficient = coffee_maker.is_resource_sufficient(drink)
        if sufficient:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)