MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino" : {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 900,
    "milk":600,
    "coffee": 300
}

def get_option(available_coffee):
    user_option = input(f"What would you like? ({'/'.join(available_coffee)}): ")
    return user_option

def print_report(machine_resources, machine_money):
    print(f"Water: {machine_resources["water"]}ml")
    print(f"Milk: {machine_resources["milk"]}ml")
    print(f"Coffee: {machine_resources["coffee"]}g")
    print(f"Money: ${money:.2f}")

def check_resources(machine_resources, coffee_menu):
    available_coffee = []
    for coffee_type in coffee_menu:
        ingredients_required = coffee_menu[coffee_type]["ingredients"]
        water_ok = ingredients_required["water"] <= machine_resources["water"]
        milk_ok = ingredients_required["milk"] <= machine_resources["milk"]
        coffee_ok = ingredients_required["coffee"] <= machine_resources["coffee"]
        if water_ok and milk_ok and coffee_ok:
            available_coffee.append(coffee_type)
    return available_coffee

def process_coins(coffee_cost, coffee_type):
    EACH_QUARTER = 0.25
    EACH_DIME = 0.10
    EACH_NICKEL = 0.05
    EACH_PENNY = 0.01
    print(f"Thanks. It's gonna be ${coffee_cost:.2f}. Please insert coins.")
    quarters = int(input("How many quarters ($0.25)?: "))
    dimes = int(input("How many dimes ($0.10)?: "))
    nickels = int(input("How many nickels ($0.05)?: "))
    pennies = int(input("How many pennies ($0.01)?: "))
    coins_total = EACH_QUARTER * quarters + EACH_DIME * dimes
    coins_total += EACH_NICKEL * nickels + EACH_PENNY * pennies
    if coins_total > coffee_cost:
        change = coins_total - coffee_cost
        print(f"Here is ${change:.2f} in change.")
        coins_profit = coffee_cost
        transaction_success = True
    elif coins_total == coffee_cost:
        coins_profit = coffee_cost
        transaction_success = True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        coins_profit = 0
        transaction_success = False
    return coins_profit, transaction_success

def make_coffee(machine_resources, coffee_menu, coffee_type):
    ingredients_required = coffee_menu[coffee_type]["ingredients"]
    water_required = ingredients_required["water"]
    milk_required = ingredients_required["milk"]
    coffee_required = ingredients_required["coffee"]
    machine_resources["water"] -= water_required
    machine_resources["milk"] -= milk_required
    machine_resources["coffee"] -= coffee_required
    print(f"Your {coffee_type} is ready. Enjoy!")
    return machine_resources

money = 0
machine_on = True

while machine_on:
    available_options = check_resources(resources, MENU)
    if not available_options:
        print("All coffee are sold out.")
        machine_on = False
    else:
        option = get_option(available_options)
        if option == "off":
            machine_on = False
        elif option == "report":
            print_report(resources, money)
        elif option in available_options:
            cost = MENU[option]["cost"]
            profit, is_success = process_coins(cost, option)
            money += profit
            if is_success:
                resources = make_coffee(resources, MENU, option)
        else:
            print(f"Sorry. {option} is not on the menu.")
