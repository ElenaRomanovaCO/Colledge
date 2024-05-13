from datetime import datetime

class Item:
    """
    Represents an item for sale with name, description, price, and quantity.
    """
    def __init__(self, item_name=None, item_description=None, item_price=0, item_quantity=0):
        self.item_name = item_name # Name of the item for the Shopping Cart
        self.item_description = item_description # Description of the item
        self.item_price = item_price # Price per unit of the item
        self.item_quantity = item_quantity # Quantity of the each item in the cart

class ShoppingCart:
    """
    Manages a shopping cart with operations to add, remove, and modify items.
    It also provides functionality to print the total cost and descriptions of items in the cart.
    """
    def __init__(self, customer_name=None, current_date="January 1, 2020"):
        self.customer_name = customer_name # Name of the customer that does shopping
        self.current_date = current_date # Date of the shopping
        self.cart_items = [] # List of items (instances of Item class) in the shopping cart

    def add_item(self, item_to_purchase):
        """
         Adds an item to the shopping cart.
         Parameters:
         item_to_purchase (Item): The item to be added to the cart.
         """
        self.cart_items.append(item_to_purchase) # Add the item object to the cart_items list
        print(f"Item {item_to_purchase.item_name} added to cart.") # Notify that the item has been added

    def remove_item(self, item_name):
        """
        Removes an item from the shopping cart by name.
        Parameters:
        item_name (str): The name of the item to be removed from the cart.
        """
        for item in self.cart_items:
            if item.item_name == item_name: # Check if the item name matches the one to be removed
                self.cart_items.remove(item)  # Remove the item from the cart_items list
                print(f"Item {item_name} removed from cart.")  # Notify that the item has been removed
                return
        print("Item not found in cart. Nothing removed.") # If no item found, notify that nothing was removed

    def modify_item(self, item_to_purchase):
        """
        Modifies the details of an existing item in the shopping cart.
        Parameters:
        item_to_purchase (Item): The item with updated details to replace the existing item.
        """
        for cart_item in self.cart_items:  # Check if the item exists in the cart
            # Update the item's description, price, and quantity if new values are provided
            if cart_item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_description != "none":
                    cart_item.item_description = item_to_purchase.item_description  # Update description
                if item_to_purchase.item_price != 0:
                    cart_item.item_price = item_to_purchase.item_price  # Update price
                if item_to_purchase.item_quantity != 0:
                    cart_item.item_quantity = item_to_purchase.item_quantity  # Update quantity
                print(f"Item {cart_item.item_name} updated.")  # Notify that the item has been updated
                return
        print("Item not found in cart. Nothing modified.")  # Notify if no matching item was found


# get_num_items_in_cart()
# Returns quantity of all items in cart. Has no parameters.
# get_cost_of_cart()
# Determines and returns the total cost of items in cart. Has no parameters.

    def get_num_items_in_cart(self):
        """
        Returns the total quantity of all items in the shopping cart.

        Returns:
            int: The total quantity of items in the cart.
        """
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        """
        Calculates and returns the total cost of all items in the shopping cart.

        Returns:
            float: The total cost of items in the cart.
        """
        total_cost = 0
        for item in self.cart_items:
            cost = item.item_price * item.item_quantity
            total_cost += cost
        return total_cost

    def print_descriptions(self):
        """
        Outputs descriptions of all items in the shopping cart.
        """
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY") # Notify if the cart is empty and exit the method
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}") # Print header with customer name and date
        print("Item Descriptions") # Print section title for item descriptions
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}") # Print each item's name and description

    def print_total(self):
        """
        Outputs the total cost of all items in the shopping cart, including a breakdown of each item's cost.
        """
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")  # Notify if the cart is empty and exit the method
            return

        # Print the cart header with customer name and date
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")

        # Display the total number of items in the cart
        total_items = self.get_num_items_in_cart()
        print(f"Number of Items: {total_items}")

        total_cost = self.get_cost_of_cart()  # Get the total cost of the cart

        for item in self.cart_items:
            cost = item.item_price * item.item_quantity  # Calculate cost for each item
            # Print the cost calculation for each item
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${cost}")

        print(f"Total: ${total_cost}")  # Display the final total cost

def print_menu(cart):
    """
    Displays a menu to interact with the shopping cart and handles user input for various actions.

    Parameters:
    cart (ShoppingCart): The shopping cart object on which operations are to be performed.

    The menu allows users to:
    - 'a': Add an item to the cart.
    - 'r': Remove an item from the cart.
    - 'c': Change the quantity of an existing item.
    - 'i': Output descriptions of all items in the cart.
    - 'o': Output the total cost and breakdown of items in the cart.
    - 'q': Quit the menu and exit the program.

    Inputs are taken repeatedly until the user decides to quit ('q').
    """

    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").lower()
        if choice == 'q':
            print("Exiting the program.")
            break
        elif choice == 'a':
            item_name = input("Enter item name: ")
            item_description = input("Enter item description: ")
            item_price = float(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            cart.add_item(Item(item_name, item_description, item_price, item_quantity))
        elif choice == 'r':
            item_name = input("Enter item name to remove: ")
            cart.remove_item(item_name)
        elif choice == 'c':
            item_name = input("Enter the item name to modify: ")
            item_description = input("Enter new description (or 'none' to keep current): ")
            try:
                item_price = float(input("Enter new price (or '0' to keep current): "))
            except ValueError:
                item_price = 0  # Default to 0 if invalid input
            try:
                item_quantity = int(input("Enter new quantity (or '0' to keep current): "))
            except ValueError:
                item_quantity = 0  # Default to 0 if invalid input
            item_to_purchase = Item(item_name, item_description, item_price, item_quantity)
            cart.modify_item(item_to_purchase)

        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        else:
            print("Invalid option, please try again.")

def validate_date(date_str):
    """
    Validates and formats a date string to ensure it matches the desired format.

    Parameters:
    date_str (str): The date string to be validated and formatted.

    Returns:
    str: A formatted date string if the input is valid.
    None: If the input date string cannot be parsed, returns None.

    The function attempts to parse the date string using various date-time formats.
    If successful, it returns the date in the format 'January 1, 2020'.
    If the parsing fails (due to an unsupported format), it catches a ValueError and returns None.
    """
    date_formats = ["%B %d, %Y", "%m/%d/%Y", "%m-%d-%Y", "%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"]

    for date_format in date_formats:
        try:
            date_obj = datetime.strptime(date_str, date_format)
            return date_obj.strftime("%B %d, %Y")
        except ValueError:
            pass

    return None

def main():
    """
    Main execution function for a shopping cart application.

    This function handles the process of obtaining the customer's name and the current date with validation.
    It initializes a shopping cart with the validated customer name and date, and then displays the menu
    of the application to the user. It uses a while loop to ensure the date is entered in the correct format
    before proceeding.
    """
    customer_name = input("Enter the customer's name: ")  # Prompt user for customer's name
    current_date = None  # Initialize the current date to None

    # Loop to ensure the entered date is in the correct format
    while current_date is None:
        date_input = input("Enter the current date (e.g., 'January 1, 2020', '01/01/2020', '2020-01-01'): ")
        current_date = validate_date(date_input)  # Validate the entered date
        if current_date is None:  # Check if the date is invalid
            print("Please enter the correct date format.")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)  # Display the shopping cart menu

if __name__ == "__main__":
    main() # Execute the main function if this script is run as the main program
