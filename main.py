#!/usr/bin/env python3

from models.beverage import Beverage
from models.snack import Snack
from models.vendingMachine import VendingMachine


# Represents the main menu
main_menu_options = {
    1: "See all added items",
    2: "Add an item",
    3: "Restock an item",
    4: "Delete an item",
    5: "Buy an item",
    0: "Exit the program"
}

def print_main_menu():
    """Prints the main menu"""
    print("---------------------------------------")
    for key in main_menu_options.keys():
        print(f"{key} --- {main_menu_options[key]}")
    print("---------------------------------------")

if __name__ == "__main__":
    machine = VendingMachine()

    while True:
        print_main_menu()
        option = int(input("Enter your choice: "))

        # See all added items
        if option == 1:
            machine.print_all_items()

        # Add an item
        elif option == 2:
            type = item = None
            while type != "snack" and type != 'beverage':
                type = input("What type of item ('Snack' / 'Beverage') do you want to add? ")
                type = type.lower().strip()

            name = input("Please input a name: ")
            price = float(input("Please input a price (without a currency): "))
            quantity = input("Please input a quantity (without a unit gr/l): ")

            if type == "snack":
                item = Snack(name, price, quantity)

            elif type == "beverage":
                item = Beverage(name, price, quantity)
        
            (status, message) = machine.add_item(item)
            print(f"{status}: {message}")

        # Restock an item    
        elif option == 3:
            if machine.items:
                machine.print_all_items()
                item_name = input("Which item do you want to restock (enter the exact name)? ")
                additional_items = int(input("How many items do you want to restock (total must not exceed 10)? "))
                (status, message) = machine.restock_item(item_name, additional_items)
                print(f"{status}: {message}")
            else:
                print("error: ", "There are no item types in the vending machine!")

        # Delete an item
        elif option == 4:
            if machine.items:
                machine.print_all_items()
                item_name = input("Which item do you want to delete (enter the exact name)? ")
                (status, message) = machine.delete_item(item_name)
                print(f"{status}: {message}")
            else:
                print("error: ", "There are no item types in the vending machine!")

        # Buy an item
        elif option == 5:
            if machine.items:
                machine.print_all_items()
                item_name = input("Which item do you want to buy? ")
                (status, message) = machine.buy_item(item_name)
                print(f"{status}: {message}")
            else:
                print("error: ", "There are no item types in the vending machine!")
        
        elif option == 0:
            print("Have a good day!")
            break;
                
        else:
            print("Thats no valid option, please choose a valid option")