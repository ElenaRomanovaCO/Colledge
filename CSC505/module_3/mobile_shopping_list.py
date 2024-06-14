# This script can provide prototyping for Mobile app Shopping list backend functionality
# UI and DB integration is out of the scope for this POC.


# initializing shopping list
shopping_list = []
# initializing categories dictionionary
categories = {}

# Creating method that will be clearing shopping list and catories.
def create_shopping_list():
    print("Creating a new shopping list...")
    shopping_list.clear()
    categories.clear()

# This method will validate if list is not empty and will display items on the list
def view_shopping_list():
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item['name']} ({item['category']})")

# This method will add item to the list from user's input and category
def add_item():
    item_name = input("Enter the item name: ")
    category = input("Enter the category (leave blank for uncategorized): ").strip()

    item = {"name": item_name, "purchased": False}
    if category:
        item["category"] = category
        categories.setdefault(category, []).append(item)
    else:
        item["category"] = "Uncategorized"
        categories.setdefault("Uncategorized", []).append(item)

    shopping_list.append(item)
    print(f"{item_name} has been added to the shopping list.")

# This method will mark item as being purchased.
def mark_item_purchased():
    view_shopping_list()
    item_index = int(input("Enter the index of the item to mark as purchased: "))
    if 0 <= item_index < len(shopping_list):
        item = shopping_list[item_index]
        item["purchased"] = True
        print(f"{item['name']} has been marked as purchased.")
    else:
        print("Invalid item index.")

# This method will assign categories to shopping list items
def categorize_items():
    view_shopping_list()
    category_name = input("Enter the category name: ")
    for item in shopping_list:
        if item["category"] == "Uncategorized":
            item["category"] = category_name
            categories.setdefault(category_name, []).append(item)
            categories["Uncategorized"].remove(item)
    print(f"Items have been categorized under '{category_name}'.")

# This method will enable sharing shoping list
def share_shopping_list():
    print("Sharing the shopping list...")
    view_shopping_list()

# Printing user instruction
while True:
    print("\nShopping List Manager")
    print("1. Create Shopping List")
    print("2. View Shopping List")
    print("3. Add Item to Shopping List")
    print("4. Mark Item as Purchased")
    print("5. Categorize Items")
    print("6. Share Shopping List")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_shopping_list()
    elif choice == "2":
        view_shopping_list()
    elif choice == "3":
        add_item()
    elif choice == "4":
        mark_item_purchased()
    elif choice == "5":
        categorize_items()
    elif choice == "6":
        share_shopping_list()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
