menu = {
    "espresso": 2.5,
    "latte": 3.0,
    "cappuccino": 3.5,
    "americano": 2.0,
    "mocha": 4.0
}

def take_order():
    print("Welcome to the Coffee Shop!")
    print("Here's our menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

    order = input("What would you like to order? ").lower()
    if order in menu:
        return order
    else:
        print("Sorry, we don't have that item on the menu.")
        return None

def calculate_total(items):
    total = 0
    for item in items:
        total += menu[item]
    return total

def main():
    orders = []
    while True:
        order = take_order()
        if order:
            orders.append(order)
            another = input("Would you like to order something else? (yes/no) ").lower()
            if another != "yes":
                break

    total_cost = calculate_total(orders)
    print("\nYour order:")
    for item in orders:
        print(item)
    print(f"Total cost: ${total_cost:.2f}")
    print("Thank you for visiting the Coffee Shop!")

if __name__ == "__main__":
    main()
