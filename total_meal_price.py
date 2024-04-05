"""
Part 1. Write a program that calculates the total amount of a meal purchased at a restaurant.
The program should ask the user to enter the charge for the food and then calculate the amounts
with an 18 percent tip and 7 percent sales tax. Display each of these amounts and the total price.
"""


def calculate_total_meal_price():
    # Inputing initial price without tax and tip
    initial_meal_charge = float(input("Enter initial charge for the meal: $"))

    # Calculating tip amount =  18%
    tip_amount = 0.18 * initial_meal_charge

    # Calculating sales tax amount = 7%
    sales_tax_amount = 0.07 * initial_meal_charge

    # Calculating total meal price
    total_meal_price = initial_meal_charge + tip_amount + sales_tax_amount

    # Displaying the amounts
    print(f"Initial Meal Charge: ${initial_meal_charge:.2f}")
    print(f"Tip Amount (18%): ${tip_amount:.2f}")
    print(f"Sales Tax Amount (7%): ${sales_tax_amount:.2f}")
    print(f"Total Meal Price: ${total_meal_price:.2f}")


# Calling the function to run the program
calculate_total_meal_price()
