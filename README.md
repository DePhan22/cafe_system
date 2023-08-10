# cafe_system
# Coffee Shop Python Program

Welcome to the Coffee Shop Python Program! This program simulates a simple coffee shop where customers can place orders from a menu, calculate the total cost, and receive an order summary.

## Getting Started

1. Make sure you have Python installed on your computer.

2. Download or clone the repository to your local machine.

3. Open a terminal/command prompt and navigate to the directory where the program files are located.

4. Run the program by executing the following command:

    ```
    python coffee_shop.py
    ```

5. Follow the prompts to place orders and interact with the program.

## How to Use

1. When you run the program, you will be presented with the coffee shop menu.

2. Enter the name of the item you'd like to order. The program will validate your choice against the menu items.

3. If your order is valid, you will be asked if you want to order anything else. Enter "yes" or "no" accordingly.

4. Once you're done ordering, the program will display your order summary along with the total cost.

5. Thank you for visiting the Coffee Shop!

## Customization

You can easily customize the menu items and their prices by editing the `menu` dictionary in the `coffee_shop.py` file. Add or remove items as needed.

```python
menu = {
    "espresso": 2.5,
    "latte": 3.5,
    "cappuccino": 3.5,
    "americano": 2.0,
    "mocha": 4.5
}
